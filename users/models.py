from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

interests = (
    ('Hood', 'Hood'),
    ('Teen', 'Teen'),
    ('Den', 'Den'),
    ('Thigh', 'Thigh'),
)
class CustomUser(AbstractUser):
    interest = models.CharField(choice=interests)
    is_teacher = models.BooleanField('Teacher', default=False)
    is_student = models.BooleanField('Student', default=False)