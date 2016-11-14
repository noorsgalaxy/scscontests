from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contests(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    catagory = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name + ' | ' + str(self.start_time)