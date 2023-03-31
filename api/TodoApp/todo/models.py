from django.db import models

# Create your models here.
class WorkTodo(models.Model):
    WORKTODO = 'worktodo'
    WORKDONE = 'workdone'

    STATUS_CHOICES = (
        (WORKTODO, 'Work To Do'),
        (WORKDONE, 'Work Done')
    )

    work_description = models.CharField(max_length=255)
    work_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=WORKTODO)
