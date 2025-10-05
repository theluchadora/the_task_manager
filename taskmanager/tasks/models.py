from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
PRIORITY_CHOICES = (
    ('Low','Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
)

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    completed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == 'Completed' and not self.completed_at:
            self.completed_at = timezone.now()
        elif self.status == 'Pending':
            self.completed_at = None
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.title} ({self.user.username})"