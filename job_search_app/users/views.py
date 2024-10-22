from .models import Job, Resume
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import HRRegistrationForm, CustomAuthenticationForm, UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def hr_register(request):
    if request.method == 'POST':
        form = HRRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = HRRegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'role': 'HR'})

def jobseeker_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create user instance but don’t save to DB yet
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Now save the user
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'role': 'Job Seeker'})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on user role
                if user.role == 'HR':
                    return redirect('hr_dashboard')  # Redirect to HR dashboard
                else:
                    return redirect('job_list')  # Redirect to job list for Job Seekers
            else:
                form.add_error(None, 'Invalid username or password.')  # Add error to form if auth fails
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def hr_dashboard(request):
    # Fetch the jobs posted by the HR
    jobs = Job.objects.all()  # Modify to filter by the current HR if needed
    resumes = Resume.objects.all()  # Fetch all resumes

    return render(request, 'users/hr_dashboard.html', {
        'jobs': jobs,
        'resumes': resumes,
    })


@login_required
def hr_dashboard(request):
    if request.user.role != 'HR':
        return HttpResponseForbidden("You are not authorized to view this page.")
    
    # HR dashboard logic
    return render(request, 'users/hr_dashboard.html')

@login_required
def job_list(request):
    query = request.GET.get('search')  # Get the search query from the URL
    if query:
        jobs = Job.objects.filter(title__icontains=query)  # Filter jobs by title
    else:
        jobs = Job.objects.all()  # If no search query, show all jobs
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

