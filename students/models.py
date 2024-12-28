from django.db import models
from groups.models import Group

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')
