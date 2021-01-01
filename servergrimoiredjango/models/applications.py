# -*- coding: utf-8 -*-
import requests
from django.db import models
import logging
from base64 import urlsafe_b64encode

from servergrimoiredjango.errors import GitLabTokenAbsent
from servergrimoiredjango.models import LabelGroupMixin

logger = logging.getLevelName(__name__)


class GitLabInstallation(LabelGroupMixin):
    base_url = models.GenericIPAddressField(unique=True)
    token = models.CharField(max_length=40, null=True, blank=True)
    version = models.CharField(max_length=60, null=True, blank=True)
    revision = models.CharField(max_length=60, null=True, blank=True)
    update = models.BooleanField(default=None, null=True, blank=True)

    def __str__(self):
        return f"GitLab installation {self.site}"

    def get_gitlab_version(self):
        if self.token is None:
            logger.error(
                "You need to set the token for the gitlab installation"
            )
            raise GitLabTokenAbsent
        logger.info("Starting the download")
        url = self.base_url + "/api/v4/version"
        headers = {"Private-Token": self.token}
        req = requests.get(url, headers=headers)
        js = req.json()
        self.version = js["version"]
        self.revision = js["revision"]
        self.save()
        return js

    def last_version_gitlab(self):
        if self.version is None:
            self.get_gitlab_version()

        gfg = urlsafe_b64encode(str.encode(f'{"version":"{self.version}"}'))
        logger.debug(gfg)
        r = requests.get(
            url="https://version.gitlab.com/check.svg",
            params={"gitlab_info": gfg},
            headers={"Referer": self.base_url},
        )
        self.update = "up-to-date" in r.text
        self.save()
        return "up-to-date" in r.text
