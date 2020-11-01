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
    day_before_allert = models.PositiveIntegerField(default=30, blank=True, null=True)

    server_connected = models.ForeignKey(
        "Server", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.domain_name} {self.ip}"

    @staticmethod
    def __check_date(will_expire_in, days_num):
        if will_expire_in and days_num:
            now = datetime.datetime.now()
            limit = now + datetime.timedelta(days=days_num)
            if now > will_expire_in:
                output_strng = {
                    "status": "KO",
                    "expired": str(will_expire_in),
                }
            elif will_expire_in < limit:
                output_strng = {
                    "status": "KO",
                    "expired": str(will_expire_in),
                }
            elif will_expire_in < limit:
                output_strng = {
                    "status": "XX",
                    "expired": str(will_expire_in),
                }
            else:
                output_strng = {
                    "status": "OK",
                    "expired": str(will_expire_in),
                }
        else:
            output_strng = {"status": "KO", "expired": "****-**-**"}
        return output_strng

    def stats_ssl(self) -> dict:
        dict_out = {}
        ssl_end_date = self.ssl_end_date if self.ssl_end_date else "****-**-** **:**:**"
        ssl_valid = Domain.__check_date(self.ssl_end_date, self.day_before_allert)
        dict_out["ssl_check"] = {"status": ssl_valid, "expired": ssl_end_date}
        return dict_out

    def stats_domain(self) -> dict:
        dict_out = {}
        domain_end_date = (
            self.domain_end_date if self.domain_end_date else "****-**-** **:**:**"
        )
        domain_valid = Domain.__check_date(self.ssl_end_date, self.day_before_allert)
        dict_out["dns_checker"] = {"status": domain_valid, "expired": domain_end_date}
        return dict_out


class Server(LabelGroupMixin, IpModelMixin, models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"Server {self.name}, local Ip {self.internal_ip}"
