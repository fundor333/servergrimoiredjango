# -*- coding: utf-8 -*-
from django.db import models


class LabelMixin:
    labels = models.ManyToManyField("Label")


class CustomGroupMixin:
    labels = models.ManyToManyField("CustomGroup")


class LabelGroupMixin(LabelMixin, CustomGroupMixin):
    pass
