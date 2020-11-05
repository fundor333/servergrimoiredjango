from django.db import models
import datetime

from servergrimoire.models.mixin import LabelGroupMixin


class IpModelMixin:
    internal_ip = models.GenericIPAddressField(null=True, blank=True)
    external_ip = models.GenericIPAddressField(null=True, blank=True)


class Domain(LabelGroupMixin, models.Model):
    domain_name = models.GenericIPAddressField(null=True, blank=True)
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
    def __check_date(will_expire_in: datetime.date, days_num: int):
        if will_expire_in and days_num:
            now = datetime.datetime.now().date()
            flag_day = now + datetime.timedelta(days=days_num)

            if will_expire_in >= now:
                if will_expire_in <= flag_day:
                    output_strng = {
                        "status": "XX",
                        "expired": str(will_expire_in),
                    }
                else:
                    output_strng = {
                        "status": "OK",
                        "expired": str(will_expire_in),
                    }
            elif will_expire_in < now:
                output_strng = {
                    "status": "KO",
                    "expired": str(will_expire_in),
                }
            else:
                output_strng = {
                    "status": "KO",
                    "expired": str(will_expire_in),
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
            self.ssl_end_date, self.day_before_allert
        )
        return domain_valid


class Server(LabelGroupMixin, IpModelMixin, models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"Server {self.name}, local Ip {self.internal_ip}"
