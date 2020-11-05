import datetime
import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestModelDomani:
    def setUp(self):
        from servergrimoire.models import Domain

        now = datetime.datetime.now().date()
        days = [0, 25, -25, 300]
        Domain.objects.create(ssl_end_date=None, domain_end_date=None)
        for day in days:
            Domain.objects.create(
                ssl_end_date=now + datetime.timedelta(days=day),
                domain_end_date=now + datetime.timedelta(days=day),
            )

    def test_status_ssl(self):
        from servergrimoire.models import Domain

        self.setUp()
        for d in Domain.objects.all():
            stats = d.stats_ssl()
            if d.ssl_end_date is None:
                assert stats["status"] == "KO"
            elif d.day_before_allert is None:
                assert stats["status"] == "KO"
            else:
                now = datetime.datetime.now().date()
                days = d.day_before_allert
                expiration = d.ssl_end_date

                flag = (expiration - now).days

                if flag < 0:
                    assert stats["status"] == "KO"
                elif flag <= days:
                    print(d.ssl_end_date)
                    assert stats["status"] == "XX"
                elif flag > days:
                    assert stats["status"] == "OK"

    def test_status_domain(self):
        from servergrimoire.models import Domain

        self.setUp()
        for d in Domain.objects.all():
            stats = d.stats_domain()
            if d.domain_end_date is None:
                assert stats["status"] == "KO"
            elif d.day_before_allert is None:
                assert stats["status"] == "KO"
            else:
                now = datetime.datetime.now().date()
                days = d.day_before_allert
                expiration = d.domain_end_date

                flag = (expiration - now).days

                if flag < 0:
                    assert stats["status"] == "KO"
                elif flag < days:
                    assert stats["status"] == "XX"
                elif flag >= days:
                    assert stats["status"] == "OK"
