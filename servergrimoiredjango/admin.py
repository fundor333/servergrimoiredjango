# -*- coding: utf-8 -*-
from django.contrib import admin

from servergrimoiredjango.models import (
    Server,
    GitLabInstallation,
    Label,
    CustomGroup,
)
from servergrimoiredjango.task import (
    task_dns_check,
    task_ssl_check,
    Domain,
    task_gitlab,
)


def task_dns_check_admin(modeladmin, request, queryset):
    for e in queryset:
        task_dns_check(e)


def task_ssl_check_admin(modeladmin, request, queryset):
    for e in queryset:
        task_ssl_check(e)


def task_gitlab_admin(modeladmin, request, queryset):
    for e in queryset:
        task_gitlab(e)


task_dns_check_admin.short_description = "Run DNS check"
task_ssl_check_admin.short_description = "Run SSL check"
task_gitlab_admin.short_description = "Run Gitlab check"


class DomainAdmin(admin.ModelAdmin):
    list_display = ["domain_name", "ip", "organizzation"]
    search_fields = ["domain_name", "ip", "organizzation"]
    ordering = ["domain_name"]
    actions = [task_dns_check_admin, task_ssl_check_admin]


class GitLabInstallationAdmin(admin.ModelAdmin):
    ordering = ["base_url"]
    list_display = ["base_url", "token"]
    search_fields = ["base_url", "token"]


class ServerAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "internal_ip", "external_ip"]
    search_fields = ["name", "internal_ip", "external_ip"]
    actions = [task_gitlab_admin]


class LabelAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "color_bk", "color_fn"]
    search_fields = ["name", "color_bk", "color_fn"]


class CustomGroupAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "color_bk", "color_fn"]
    search_fields = ["name", "color_bk", "color_fn"]


admin.site.register(Domain, DomainAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(GitLabInstallation, GitLabInstallationAdmin)
