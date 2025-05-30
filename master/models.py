import uuid
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Department(models.Model):
    dep_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Department ID')

    created_by = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL,
                                   null=True, blank=True,  related_name='departments_created', verbose_name='Created By')
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='Created At')

    updated_by = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='departments_updated', verbose_name='Updated By')

    updated_at = models.DateTimeField(
        null=True, blank=True, verbose_name='Updated At')

    dep_name = models.CharField(
        max_length=200, null=True, blank=False, unique=True, verbose_name='Department Name')

    def __str__(self):
        return self.dep_name


class Project(models.Model):
    project_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Project ID')

    created_by = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='projects_created', verbose_name='Created By')
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='Created At')

    updated_by = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='projects_updated', verbose_name='Updated By')

    updated_at = models.DateTimeField(
        null=True, blank=True, verbose_name='Updated At')

    project_name = models.CharField(
        max_length=200, unique=True, null=True, blank=False, verbose_name='Project Name')

    assigned_dep = models.ManyToManyField(
        Department, blank=False, verbose_name='Assigned Departments')

    responsible_persons = models.ManyToManyField(
        'accounts.CustomUser', help_text="Select users who are responsible for this project", related_name='projects_responsible', verbose_name='Responsible Persons')

    def __str__(self):
        return self.project_name
