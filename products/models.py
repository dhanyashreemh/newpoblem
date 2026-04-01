from django.db import models


class Product(models.Model):
    shopify_id = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=255)

    class Meta:
        db_table = "products"   # custom table name
        ordering = ["-id"]      # latest first
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title


class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    shopify_variant_id = models.BigIntegerField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "variants"
        ordering = ["-id"]
        unique_together = ["product", "shopify_variant_id"]

    def __str__(self):
        return f"{self.product.title} - {self.shopify_variant_id}"