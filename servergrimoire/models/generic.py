from colorfield.fields import ColorField
from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=300)
    color_bk = ColorField(default='#FF0000')
    color_fn = ColorField(default='#FF0000')

    def __str__(self):
        return self.name


class IpModelMixin:
    internal_ip = models.GenericIPAddressField(null=True, blank=True)
    external_ip = models.GenericIPAddressField(null=True, blank=True)


class LabelMixin:
    labels = models.ManyToManyField("Label")


class Domain(LabelMixin, models.Model):
    domain_name = models.GenericIPAddressField(null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    ssl_valid = models.BooleanField(default=False)
    ssl_end_date = models.DateField(null=True,blank=True)
    domain_end_date  = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.domain_name} {self.ip}"


class Server(LabelMixin, IpModelMixin, models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"Server {self.name}, local Ip {self.internal_ip}"
