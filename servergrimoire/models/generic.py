from colorfield.fields import ColorField
from django.db import models

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=300)
    color_bk = ColorField(default='#FF0000')
    color_fn = ColorField(default='#FF0000')

    def __str__(self):
        return self.name

class IpModelMixin:
    internal_ip= models.GenericIPAddressField(null=True, blank=True)
    external_ip= models.GenericIPAddressField(null=True, blank=True)

class LabelMixin:
    labels = models.ManyToManyField("Label")
