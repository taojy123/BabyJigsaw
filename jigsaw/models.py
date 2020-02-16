from django.db import models


class Picture(models.Model):
    pic = models.ImageField(upload_to='pics')
    p1 = models.ImageField(upload_to='pics', null=True, blank=True)
    p2 = models.ImageField(upload_to='pics', null=True, blank=True)
    p3 = models.ImageField(upload_to='pics', null=True, blank=True)
    p4 = models.ImageField(upload_to='pics', null=True, blank=True)

