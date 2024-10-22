# Generated by Django 5.1.2 on 2024-10-21 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_hr',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_job_seeker',
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('HR', 'HR'), ('JobSeeker', 'Job Seeker')], default='JobSeeker', max_length=10),
        ),
    ]
