from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from unicodedata import name
from django.db import models
# from django.contrib.auth import get_user_model

from datetime import datetime

import uuid

class StudProfile(models.Model):
    user=models.CharField(max_length=100)
    regId=models.CharField(max_length=10)
    profileImg=models.ImageField(upload_to="profile_images",default="img-01.png")
    bio=models.TextField(blank=True)
    emaill=models.CharField(max_length=100,blank=True)
    done=models.BooleanField(default=False,blank=True)


class ClubProfile(models.Model):
    clubname = models.CharField(max_length=100,default="")
    logo = models.ImageField(upload_to="profile_images",default="")
    des=models.TextField(blank=True,default="")
    clubId = models.CharField(max_length=10,default="")
    cemaill=models.CharField(max_length=100,blank=True,default="")

class Posts(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    username = models.CharField(max_length=100,default="")
    imagee = models.ImageField(upload_to='post_images',default='img-01.png')
    createdAt=models.DateTimeField(default=datetime.now)
    venue = models.CharField(max_length=1000,default="")
    deadLine = models.DateTimeField(default=datetime.now)
    des = models.TextField(blank=True,default="")
    phone = models.IntegerField(default=0)
    cntemail = models.CharField(max_length=100)



