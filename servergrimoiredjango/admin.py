# -*- coding: utf-8 -*-
from django.contrib import admin

from servergrimoiredjango.models import Server, GitLabInstallation
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
    list_display = ["domain_name", "ip"]
    search_fields = ["domain_name", "ip"]
    ordering = ["domain_name"]
    actions = [task_dns_check_admin, task_ssl_check_admin]


class GitLabInstallationAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["domain_name", "ip"]
    search_fields = ["domain_name", "ip"]


class ServerAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["base_url", "version", "revision", "token"]
    search_fields = ["base_url", "version", "revision", "token"]
    actions = [task_gitlab_admin]


admin.site.register(Domain, DomainAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(GitLabInstallation, GitLabInstallationAdmin)
