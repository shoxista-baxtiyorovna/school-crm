from django.db import models
from teachers.models import Teacher


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, related_name='group')
