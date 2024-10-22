from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('HR', 'HR'),
        ('JobSeeker', 'Job Seeker'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='JobSeeker')

    def __str__(self):
        return self.username

    # Add unique related_names to avoid reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # ForeignKey to CustomUser
    job = models.ForeignKey(Job, on_delete=models.CASCADE)  # ForeignKey to Job
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f"{self.user.username}'s resume for {self.job.title}"
