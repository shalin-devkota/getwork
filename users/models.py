from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import ModelState
from django.shortcuts import get_object_or_404


class Profile(models.Model):
    user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    about_me = models.TextField(max_length=250,blank=False)
    jobs_accepted = models.IntegerField(default=0)
    offers_created = models.IntegerField(default=0)
    profile_picture = models.ImageField(default="default_pp.png",upload_to="profile_pics")
    cover_picture = models.ImageField(default="default_cp.png",upload_to="cover_pics")

    def __str__(self):
        return self.email

