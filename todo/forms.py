from django import forms
from django.forms import ModelForm
from .models import *
from ckeditor.widgets import CKEditorWidget


class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'assigned_to',
                  'task_priority', 'task_status', 'due_date', 'document_upload']

        widgets = {

            "task_name": forms.TextInput(attrs={"class": "form-control", 'required': 'true', }),
            "description": forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Write your task overview'})),
            "assigned_to": forms.Select(attrs={"class": "form-control"}),
            "task_priority": forms.Select(attrs={"class": "form-control"}),
            "task_status": forms.Select(attrs={"class": "form-control"}),
            "due_date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "document_upload": forms.FileInput(attrs={"class": "form-control"})

        }
