# -*- coding: utf-8 -*-
from django.db import models


class Notifications(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image = models.FileField(upload_to='')
    name = models.CharField(max_length=255)
