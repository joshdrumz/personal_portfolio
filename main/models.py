from django.db import models
from datetime import datetime

# Create your models here.


class Project(models.Model):
    project_title = models.CharField(max_length=20)
    project_content = models.TextField()
    project_host = models.URLField(max_length=200, default='', blank=True)
    project_code = models.URLField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.project_title
