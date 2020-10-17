from django.db import models

from servergrimoire.models.mixin import LabelMixin


class IpModelMixin:
    internal_ip = models.GenericIPAddressField(null=True, blank=True)
    external_ip = models.GenericIPAddressField(null=True, blank=True)


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
