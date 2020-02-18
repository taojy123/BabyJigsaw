from django.db import models


class Picture(models.Model):
    token = models.CharField(max_length=64, blank=True)
    pic = models.ImageField(upload_to='pics')

