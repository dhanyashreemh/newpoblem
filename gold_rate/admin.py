from django.contrib import admin
from .models import GoldRate, MakingCharges, TaxConfig

admin.site.register(GoldRate)

@admin.register(TaxConfig)
class TaxConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not TaxConfig.objects.exists()


@admin.register(MakingCharges)
class MakingChargesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not MakingCharges.objects.exists()