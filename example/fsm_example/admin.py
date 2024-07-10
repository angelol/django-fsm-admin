from django.contrib import admin

from fsm_admin.mixins import FSMTransitionMixin
from fsm_example.models import PublishableModel


# Example use of FSMTransitionMixin (order is important!)
@admin.register(PublishableModel)
class PublishableModelAdmin(FSMTransitionMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "display_from",
        "display_until",
        "state",
    )
    list_filter = ("state",)
    readonly_fields = ("state",)
