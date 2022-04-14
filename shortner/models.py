from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.URLField()
    uuid = models.CharField(max_length=15, unique=True)
    created = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.link