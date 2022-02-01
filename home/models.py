from django.db import models

class menu(models.Model):
      dishname=models.CharField(max_length=120)
      price=models.CharField(max_length=12)
