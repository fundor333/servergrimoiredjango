# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path

from servergrimoiredjango.views import GrimoireDashboard, GrimoireDomainView

urlpatterns = [
    path("domain/", GrimoireDashboard.as_view(), name="grimoire_domain_list"),
    path(
        "domain/add", GrimoireDashboard.as_view(), name="grimoire_domain_add"
    ),
    path(
        "domain/<int:pk>",
        GrimoireDomainView.as_view(),
        name="grimoire_domain_view",
    ),
    path("", GrimoireDashboard.as_view(), name="grimoire_dashboard"),
]
