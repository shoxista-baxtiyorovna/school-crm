from django.db import models
from django.shortcuts import reverse


class Subject(models.Model):
    subject_title = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_title

    def get_detail_url(self):
        return reverse('subjects:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('subjects:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('subjects:update', args=[self.pk])