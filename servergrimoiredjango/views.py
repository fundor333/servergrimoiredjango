# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from servergrimoiredjango.filters import DomainFilter
from servergrimoiredjango.models import Domain, reverse


class GrimoireDashboard(LoginRequiredMixin, FilterView):
    filterset_class = DomainFilter
    paginate_by = 20


class GrimoireDomainView(LoginRequiredMixin, DetailView):
    model = Domain


class GrimoireDomainAdd(LoginRequiredMixin, CreateView):
    model = Domain
    fields = ["domain_name", "day_before_allert", "server_connected"]

    def get_form(self, form_class=None):
        form = super(GrimoireDomainAdd, self).get_form(form_class)
        for visible in form.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
        return form


class GrimoireDomainDelete(LoginRequiredMixin, DeleteView):
    model = Domain

    def get_success_url(self):
        next = self.request.POST.get("next", False)
        if next:
            return HttpResponseRedirect(next)
        else:
            return reverse("grimoire_domain_list")


class GrimoireDomainUpdate(LoginRequiredMixin, UpdateView):
    model = Domain
    fields = [
        "domain_name",
        "day_before_allert",
        "server_connected",
        "labels",
        "groups",
    ]

    def get_form(self, form_class=None):
        form = super(GrimoireDomainUpdate, self).get_form(form_class)
        for visible in form.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
        return form
