from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'مبتدی'),
        ('intermediate', 'متوسط'),
        ('advanced', 'پیشرفته'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fitness_level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')

    def __str__(self):
        return f"{self.user.username} - {self.get_fitness_level_display()}"

class WorkoutProgram(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'مبتدی'),
        ('intermediate', 'متوسط'),
        ('advanced', 'پیشرفته'),
    ]

    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.get_level_display()})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
