from django.db import models

class PricingConfig(models.Model):
    gold_22k = models.FloatField()
    gold_24k = models.FloatField()
    gst_percent = models.FloatField()
    making_charge = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure only one record exists
        self.__class__.objects.all().delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Pricing Configuration"

    class Meta:
        verbose_name = "Pricing Configuration"
        verbose_name_plural = "Pricing Configuration"