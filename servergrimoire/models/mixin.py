from django.db import models


class LabelMixin:
    labels = models.ManyToManyField("Label")


class CustomGroupMixin:
    labels = models.ManyToManyField("CustomGroup")
