# -*- coding: utf-8 -*-
from django.db import models


class LabelMixin(models.Model):
    labels = models.ManyToManyField("Label")

    class Meta:
        abstract = True


class CustomGroupMixin(models.Model):
    groups = models.ManyToManyField("CustomGroup")

    class Meta:
        abstract = True


class LabelGroupMixin(LabelMixin, CustomGroupMixin):
    pass
