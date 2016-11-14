from __future__ import unicode_literals

from django.db import models
from allauth.socialaccount.models import SocialAccount
from ..contests.models import Contests
# Create your models here.


class UserInfo(models.Model):
    user = models.ForeignKey(SocialAccount)
    username = models.CharField(max_length=100,default="Set Your Username")
    email = models.EmailField()
    about = models.TextField(max_length=1000,default="Edit Profile")
    college = models.CharField(max_length=500,default="Sant Longowal Institute of Engineering and Technology")
    branch = models.CharField(max_length=100,default="Computer Science Engineering")
    contest_registered = models.ManyToManyField(Contests)

    def __str__(self):
        return str(self.user.extra_data['name'])



