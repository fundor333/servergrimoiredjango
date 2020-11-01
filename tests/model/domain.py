import datetime
from django.test import TestCase
from servergrimoire.models import Domain


class ModelDomaniTest(TestCase):
    def setUp(self):
        now = datetime.datetime.now()
        days = [0, 25, -25, 300]
        Domain.objects.create(ssl_end_date=None, domain_end_date=None)
        for day in days:
            Domain.objects.create(
                ssl_end_date=now + datetime.timedelta(days=day),
                domain_end_date=now + datetime.timedelta(days=day),
            )

    def test_status_ssl(self):
        for d in Domain.objects.all():
            stats = d.stats_ssl()
            if d.ssl_end_date is None:
                self.assertEqual(stats["status", "KO"])
            elif d.day_before_allert is None:
                self.assertEqual(stats["status", "KO"])
            else:
                now = datetime.datetime.now()
                days = d.day_before_allert
                expiration = d.ssl_end_date

                flag = (expiration - now).days

                if flag < 0:
                    self.assertEqual(stats["status", "KO"])
                elif flag < days:
                    self.assertEqual(stats["status", "XX"])
                elif flag >= days:
                    self.assertEqual(stats["status", "OK"])

    def test_status_domain(self):
        for d in Domain.objects.all():
            stats = d.stats_domain()
            if d.domain_end_date is None:
                self.assertEqual(stats["status", "KO"])
            elif d.day_before_allert is None:
                self.assertEqual(stats["status", "KO"])
            else:
                now = datetime.datetime.now()
                days = d.day_before_allert
                expiration = d.domain_end_date

                flag = (expiration - now).days

                if flag < 0:
                    self.assertEqual(stats["status", "KO"])
                elif flag < days:
                    self.assertEqual(stats["status", "XX"])
                elif flag >= days:
                    self.assertEqual(stats["status", "OK"])
