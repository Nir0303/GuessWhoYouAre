from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Networks(models.Model):
    socialNetworkName=models.CharField(max_length=100)
    socialNetworkType=models.CharField(max_length=100)
    socialNetworkLogo=models.CharField(max_length=100)
    def __str__(self):
        return self.socialNetworkName