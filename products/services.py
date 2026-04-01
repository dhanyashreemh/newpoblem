from django.db import transaction
from .models import Product, Variant

def create_or_update_product(data):
    with transaction.atomic():
        product, _ = Product.objects.update_or_create(
            shopify_id=data["id"],
            defaults={
                "title": data.get("title", "")
            }
        )

        for variant in data.get("variants", []):
            Variant.objects.update_or_create(
                shopify_variant_id=variant["id"],
                defaults={
                    "product": product,
                    "price": variant.get("price", 0)
                }
            )