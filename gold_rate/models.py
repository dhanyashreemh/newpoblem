from django.db import models

class PricingConfig(models.Model):
    gold_22k = models.FloatField()
    gold_24k = models.FloatField()
    gst_percent = models.FloatField()
    making_charge = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        is_update = self.pk is not None
        super().save(*args, **kwargs)

        if is_update:
            from .services.engine import update_all_prices
            update_all_prices()

    def __str__(self):
        return "Pricing Configuration"

    class Meta:
        verbose_name = "Pricing Configuration"
        verbose_name_plural = "Pricing Configuration"