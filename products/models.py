from django.db import models
class Product(models.Model):
    shopify_id = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=255)
    body_html = models.TextField(null=True, blank=True)
    handle = models.CharField(max_length=255, null=True, blank=True)
    vendor = models.CharField(max_length=255, null=True, blank=True)
    product_type = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    published_scope = models.CharField(max_length=50, null=True, blank=True)
    tags = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)

    raw_data = models.JSONField(null=True, blank=True)  

    class Meta:
        db_table = "products"  
        ordering = ["-id"]  
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title


class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")

    shopify_variant_id = models.BigIntegerField(unique=True)

    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    compare_at_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    sku = models.CharField(max_length=255, null=True, blank=True)
    barcode = models.CharField(max_length=255, null=True, blank=True)

    inventory_quantity = models.IntegerField(null=True, blank=True)
    inventory_item_id = models.BigIntegerField(null=True, blank=True)

    taxable = models.BooleanField(default=True)
    position = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "variants"
        ordering = ["-id"]
        unique_together = ["product", "shopify_variant_id"]

    def __str__(self):
        return f"{self.product.title} - {self.shopify_variant_id}"
    
class Option(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="options"
    )

    name = models.CharField(max_length=255)
    position = models.IntegerField(null=True, blank=True)
    values = models.JSONField()

    class Meta:
        db_table = "product_options"  
        ordering = ["position"]     
        unique_together = ("product", "name") 

    def __str__(self):
        return f"{self.product.title} - {self.name}"

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )

    shopify_image_id = models.BigIntegerField(null=True, blank=True)
    src = models.URLField()

    class Meta:
        db_table = "product_images"
        ordering = ["id"]  
        indexes = [
            models.Index(fields=["shopify_image_id"]),
        ]

    def __str__(self):
        return f"Image for {self.product.title}"
    

class WebhookLog(models.Model):
    webhook_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "webhook_logs"