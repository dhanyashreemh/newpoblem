from django.contrib import admin
from .models import PricingConfig


@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not PricingConfig.objects.exists()

    list_display = ("gold_22k", "gold_24k", "gst_percent", "making_charge", "updated_at")