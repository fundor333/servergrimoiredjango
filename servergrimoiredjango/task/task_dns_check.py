# -*- coding: utf-8 -*-
import datetime
from typing import Optional

import whois

from servergrimoiredjango.models import Domain


def task_dns_check(domain: Domain) -> Optional[datetime.date]:
    w = whois.whois(domain.domain_name)
    if w["domain_name"] is None:
        return None
    else:
        domain.domain_end_date = w.expiration_date
        domain.save()
        return w.expiration_date
