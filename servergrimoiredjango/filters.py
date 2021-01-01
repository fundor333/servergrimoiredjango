# -*- coding: utf-8 -*-
from django.db.models import Q
import django_filters

from servergrimoiredjango.models import Domain


class DomainFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method="my_custom_filter")

    class Meta:
        model = Domain
        fields = ["q"]

    def my_custom_filter(self, queryset, name, value):
        return Domain.objects.filter(
            Q(loc__icontains=value)
            | Q(loc_mansioned__icontains=value)
            | Q(loc_country__icontains=value)
            | Q(loc_modern__icontains=value)
        )
