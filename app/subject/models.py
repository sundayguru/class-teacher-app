from __future__ import unicode_literals

from django.db import models


class Subject(models.Model):
  title = models.CharField(max_length=120, default='')
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-created_date']
