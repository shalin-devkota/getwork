from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Offer(models.Model):
    title = models.CharField(max_length= 150)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField(max_length=250)
    payment = models.IntegerField()
    is_taken = models.BooleanField(default =0 )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('offers-list')
        