from django.urls import path
from . import views 

urlpatterns = [
    path('register/hr/', views.hr_register, name='hr_register'),        # HR registration
    path('register/jobseeker/', views.jobseeker_register, name='jobseeker_register'),  # Job Seeker registration
    path('login/', views.login_view, name='login'),                    # Login page
    path('logout/', views.logout_view, name='logout'),                  # Logout action
    path('hr/dashboard/', views.hr_dashboard, name='hr_dashboard'),     # HR dashboard
    path('jobs/', views.job_list, name='job_list'),                          # Job listing
]

