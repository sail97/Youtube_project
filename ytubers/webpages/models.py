from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    button_text = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='media/slider/%Y/%m')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    role=models.CharField(max_length=200)
    fb_link=models.CharField(max_length=200)
    linkedin_link=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='media/team/%Y/%m')
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'