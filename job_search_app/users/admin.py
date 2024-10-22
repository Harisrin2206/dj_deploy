from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Job, Resume  

# Create an admin class for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']  # Add relevant fields
    list_filter = ['is_staff', 'is_active', 'role']  # Optional: add filters
    search_fields = ['username', 'email']  # Optional: add search functionality
    ordering = ['username']  # Optional: define ordering

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)

# Register the Job and Resume Models
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'created_at')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'file')
