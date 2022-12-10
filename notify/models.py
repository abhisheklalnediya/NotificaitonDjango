from django.db import models

# Create your models here.


class Notifications(models.Model):
  title = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  image = models.CharField(max_length=255)
  name = models.CharField(max_length=255)