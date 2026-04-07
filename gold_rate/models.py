from django.db import models

class GoldRate(models.Model):
    PURITY_CHOICES = [
        ('22K', '22K'),
        ('24K', '24K'),
    ]

    purity = models.CharField(max_length=10, choices=PURITY_CHOICES, unique=True)
    rate_per_gram = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Gold Rate"
        verbose_name_plural = "Gold Rates"

    def __str__(self):
        return f"{self.purity} - ₹{self.rate_per_gram}/g"


class TaxConfig(models.Model):
    gst_percent = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.__class__.objects.all().delete() 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"GST: {self.gst_percent}%"


class MakingCharges(models.Model):
    charge_per_gram = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Making Charges"
        verbose_name_plural = "Making Charges"

    def save(self, *args, **kwargs):
        self.__class__.objects.all().delete() 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"₹{self.charge_per_gram}/g"