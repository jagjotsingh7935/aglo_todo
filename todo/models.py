from django.db import models
from django.utils.timezone import now

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    due_date = models.DateField(null=True, blank=True)  # Optional field
    tags = models.TextField(null=True, blank=True)  # Store tags as a comma-separated string
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
