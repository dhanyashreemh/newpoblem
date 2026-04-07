from django.db import models

class PricingConfig(models.Model):
    gold_22k = models.FloatField()
    gold_24k = models.FloatField()
    gst_percent = models.FloatField()
    making_charge = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        self.__class__.objects.exclude(id=self.id).delete()

        super().save(*args, **kwargs)
        from .services.engine import update_all_prices

        print("🔥 Triggering price update...")
        update_all_prices()

    def __str__(self):
        return "Pricing Configuration"

    class Meta:
        verbose_name = "Pricing Configuration"
        verbose_name_plural = "Pricing Configuration"