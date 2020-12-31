# -*- coding: utf-8 -*-
import datetime
import socket
import ssl
from typing import Optional

from servergrimoiredjango.models import Domain


def task_ssl_check(domain: Domain) -> Optional[datetime.date]:
    try:
        ssl_date_fmt = r"%b %d %H:%M:%S %Y %Z"
        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=domain.domain_name,
        )
        conn.connect((domain.domain_name, 443))
        ssl_info = conn.getpeercert()
        ssl_date = datetime.datetime.strptime(
            ssl_info["notAfter"], ssl_date_fmt
        ).date()
        domain.ssl_end_date = ssl_date
        domain.save()
        return ssl_date
    except ResourceWarning:
        return None
    except FileNotFoundError:
        return None
    except socket.gaierror:
        return None
    except TimeoutError:
        return None
    except ssl.SSLError:
        return None
    except socket.timeout:
        return None
    except OSError:
        return None
    except ssl.CertificateError:
        return None
