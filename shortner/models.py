from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000, unique=True)
    uuid = models.CharField(max_length=15, unique=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link