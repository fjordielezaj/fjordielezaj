from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    # A foreign key relationship with the User model, allowing each task to be associated with a user.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # The title of the task, represented as a character field with a maximum length of 250 characters.
    title = models.CharField(max_length=250)
    # A description of the task, represented as a text field. It can be null and blank, meaning it's optional.
    description = models.TextField(null=True, blank=True)
    # A boolean field to indicate whether the task is complete or not. The default is set to False.
    complete = models.BooleanField(default=False)
    # A DateTimeField that automatically stores the date and time when a task is created.
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # A human-readable representation of the task. In this case, it returns the task's title.
        return self.title
    
    class Meta:
        # The default ordering of tasks. Completed tasks will be displayed first.
        ordering = ['complete']