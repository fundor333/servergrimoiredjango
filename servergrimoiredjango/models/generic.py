# -*- coding: utf-8 -*-
from colorfield.fields import ColorField
from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=300)
    color_bk = ColorField(default="#FF0000")
    color_fn = ColorField(default="#FF0000")

    def __str__(self):
        return self.name


class CustomGroup(models.Model):
    name = models.CharField(max_length=300)
    color_bk = ColorField(default="#FF0000")
    color_fn = ColorField(default="#FF0000")

    def __str__(self):
        return self.name
