from django.contrib import admin

# from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from . import models


# Taken from django-all-auth: https://django-allauth.readthedocs.io/en/latest/advanced.html#admin
# "require users to login before going to the Django admin site’s login page"
# admin.site.login = login_required(admin.site.login)


# View sessions in Django Admin.
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ["session_key", "_session_data", "expire_date"]


class AgentAdmin(admin.ModelAdmin):

    list_display = ("id", "scan_agent", "description", "api_token", "last_checkin")

    readonly_fields = ("id", "scan_agent", "api_token", "last_checkin")


class ScanCommandAdmin(admin.ModelAdmin):

    list_display = ("id", "scan_binary", "scan_command_name", "scan_command")


class ScanAdmin(admin.ModelAdmin):

    list_display = ("id", "site", "scan_name", "start_time", "recurrences")

    exclude = ("completed_time", "result_file_base_name")


class SiteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "site_name",
        "description",
        "targets",
        "excluded_targets",
        "scan_command",
        "scan_agent",
        "email_scan_alerts",
        "email_alert_address",
    )


class ScheduledScanAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "site_name",
        "site_name_id",
        "scan_id",
        "start_time",
        "scan_agent",
        "scan_agent_id",
        "start_datetime",
        "scan_binary",
        "scan_command",
        "scan_command_id",
        "targets",
        "excluded_targets",
        "scan_status",
        "completed_time",
        "result_file_base_name",
    )

    exclude = ("completed_time", "result_file_base_name")


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(Session, SessionAdmin)

_register(models.Agent, AgentAdmin)
_register(models.ScanCommand, ScanCommandAdmin)
_register(models.Scan, ScanAdmin)
_register(models.ScheduledScan, ScheduledScanAdmin)
_register(models.Site, SiteAdmin)
