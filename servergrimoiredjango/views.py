# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class GrimoireDashboard(TemplateView):
    template_name = "servergrimoiredjango/dashboard.html"
