import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    user_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    user_image = models.ImageField(
        upload_to='uploads/user_images', null=True, blank=True, verbose_name='User Image')

    TYPE_CHOICES = (
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('HR', 'HR'),
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
        ('DM Team', 'DM Team'),
        ('Intern', 'Intern'),
    )

    user_type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, null=True, blank=True, verbose_name='User Type')

    phone_no = models.CharField(
        max_length=10, null=True, blank=True, verbose_name='Phone No.')

    email = models.EmailField(null=True, blank=True,
                              unique=True, verbose_name='Email')
