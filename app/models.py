from django.db import models

# Create your models here.

class Object(models.Model):
    ip = models.GenericIPAddressField(protocol='iPv4')
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['datetime']


