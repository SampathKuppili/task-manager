import uuid
from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings

# Create your models here.


class Task(models.Model):
    task_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Task ID')

    created_at = models.DateTimeField(auto_now_add=True)

    task_name = models.CharField(
        max_length=20, null=True, blank=False, unique=True, verbose_name='Task Name')

    description = RichTextField(blank=True, null=True,
                                verbose_name='Task Description')

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Assigned Tasks"
    )

    TASK_PRIORITY = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    )

    task_priority = models.CharField(
        max_length=20, choices=TASK_PRIORITY, null=True, blank=True, verbose_name='Task Priority')

    TASK_STATUS = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('On Hold', 'On Hold'),
        ('Testing', 'Testing'),
        ('Completed', 'Completed')
    )

    task_status = models.CharField(
        max_length=20, choices=TASK_STATUS, default='Not Started', null=True, blank=True, verbose_name='Task Status')

    due_date = models.DateField(
        blank=True, null=True, verbose_name='Dead line')

    document_upload = models.FileField(
        upload_to='uploads/tasks', null=True, blank=True, verbose_name='Upload Document')

    def __str__(self):
        return self.task_name
