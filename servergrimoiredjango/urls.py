# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path

from servergrimoiredjango.views import GrimoireDashboard

urlpatterns = [
    path("", GrimoireDashboard.as_view(), name="grimoire_dashboard"),
]
