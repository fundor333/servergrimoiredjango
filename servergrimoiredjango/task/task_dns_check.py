# -*- coding: utf-8 -*-
import datetime

import whois

from servergrimoiredjango.models import Domain


def task_dns_check(domain: Domain) -> datetime.date | None:
    w = whois.whois(domain.domain_name)
    if w["domain_name"] is None:
        return None
    else:
        domain.domain_end_date = w.expiration_date
        domain.save()
        return w.expiration_date
