# -*- coding: utf-8 -*-
import socket
from urllib.parse import urlparse
from django.db import models
import datetime
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver

from servergrimoiredjango.models.mixin import LabelGroupMixin


class IpModelMixin(models.Model):
    internal_ip = models.GenericIPAddressField(null=True, blank=True)
    external_ip = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        abstract = True


class Domain(LabelGroupMixin):
    domain_name = models.URLField()
    organizzation = models.CharField(max_length=200, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    ssl_end_date = models.DateField(null=True, blank=True)
    domain_end_date = models.DateField(null=True, blank=True)
    day_before_allert = models.PositiveIntegerField(
        default=30, blank=True, null=True
    )

    server_connected = models.ForeignKey(
        "Server", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.domain_name} {self.ip}"

    @staticmethod
    def __check_date(will_expire_date: datetime.date, days_num: int = 30):
        if will_expire_date:
            now = datetime.datetime.now().date()
            flag_day = now + datetime.timedelta(days=days_num)

            if will_expire_date >= now:
                if will_expire_date <= flag_day:
                    output_strng = {
                        "status": "XX",
                        "expired": str(will_expire_date),
                    }
                else:
                    output_strng = {
                        "status": "OK",
                        "expired": str(will_expire_date),
                    }
            elif will_expire_date < now:
                output_strng = {
                    "status": "KO",
                    "expired": str(will_expire_date),
                }
            else:
                output_strng = {
                    "status": "KO",
                    "expired": str(will_expire_date),
                }
        else:
            output_strng = {"status": "KO", "expired": "****-**-**"}
        return output_strng

    def stats_ssl(self) -> dict:
        ssl_valid = Domain.__check_date(
            self.ssl_end_date, self.day_before_allert
        )
        return ssl_valid

    def stats_domain(self) -> dict:
        domain_valid = Domain.__check_date(
            self.domain_end_date, self.day_before_allert
        )
        return domain_valid

    def get_absolute_url(self):
        return reverse("grimoire_domain_view", kwargs={"pk": self.pk})


@receiver(pre_save, sender=Domain)
def fix_ip(sender, instance, **kwargs):
    instance.ip = socket.gethostbyname(urlparse(instance.domain_name).netloc)


class Server(LabelGroupMixin, IpModelMixin):
    name = models.CharField(max_length=300)

    def __str__(self):
        if self.internal_ip:
            return f"Server {self.name}, local Ip {self.internal_ip}"
        else:
            return f"Server {self.name}"
