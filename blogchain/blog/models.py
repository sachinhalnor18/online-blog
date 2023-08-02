# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models herepyth
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    short_desc=models.CharField(max_length=250,default="")
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=12)
    dtext=models.TextField()
    time=models.DateTimeField(auto_now_add=True)


    