from django.db import models


class TaskState(models.TextChoices):
    PLANNED = "Planned"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class Task(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    estimate = models.IntegerField(blank=False)
    state = models.CharField(max_length=100, choices=TaskState.choices, default=TaskState.PLANNED)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['creation_date']
