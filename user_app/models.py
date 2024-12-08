from django.db import models

# Create your models here.
from django.db import models

class TaskModel(models.Model):
    name = models.CharField(max_length=255)  # Task name
    reminder_time = models.DateTimeField()  # Task reminder date and time
    is_completed = models.BooleanField(default=False)  # Task completion status
    created_at = models.DateTimeField(auto_now_add=True)  # Task creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Task update timestamp

    def __str__(self):
        return f"{self.name} - {self.reminder_time.strftime('%Y-%m-%d %H:%M')}"


from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name} ({self.email})"










