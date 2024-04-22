# models.py
from django.db import models

class Mockup(models.Model):
    company_name = models.CharField(max_length=100)
    helmet_color = models.CharField(max_length=50)
    helmet_model = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    front_logo = models.FileField(upload_to='logos/')
    back_logo = models.FileField(upload_to='logos/')
    left_logo = models.FileField(upload_to='logos/')
    right_logo = models.FileField(upload_to='logos/')
