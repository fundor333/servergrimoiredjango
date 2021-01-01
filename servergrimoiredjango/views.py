# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import DetailView
from django_filters.views import FilterView

from servergrimoiredjango.filters import DomainFilter
from servergrimoiredjango.models import Domain


class GrimoireDashboard(LoginRequiredMixin, FilterView):
    template_name = "servergrimoiredjango/dashboard.html"
    filterset_class = DomainFilter
    paginate_by = 20


class GrimoireDomainView(LoginRequiredMixin, DetailView):
    model = Domain
