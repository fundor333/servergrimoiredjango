# -*- coding: utf-8 -*-
from django.urls import path

from servergrimoiredjango.views import (
    GrimoireDashboard,
    GrimoireDomainView,
    GrimoireDomainAdd,
    GrimoireDomainUpdate,
    GrimoireDomainDelete,
)

urlpatterns = [
    path("domain/", GrimoireDashboard.as_view(), name="grimoire_domain_list"),
    path(
        "domain/add", GrimoireDomainAdd.as_view(), name="grimoire_domain_add"
    ),
    path(
        "domain/<int:pk>",
        GrimoireDomainView.as_view(),
        name="grimoire_domain_view",
    ),
    path(
        "domain/<int:pk>/update",
        GrimoireDomainUpdate.as_view(),
        name="grimoire_domain_update",
    ),
    path(
        "domain/<int:pk>/delete",
        GrimoireDomainDelete.as_view(),
        name="grimoire_domain_delete",
    ),
    path("", GrimoireDashboard.as_view(), name="grimoire_dashboard"),
]
