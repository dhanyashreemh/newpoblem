from django.utils.dateparse import parse_datetime
from .models import Product, Variant, Option


def create_or_update_product(data):
    product, _ = Product.objects.update_or_create(
        shopify_id=data["id"],
        defaults={
            "title": data.get("title"),
            "body_html": data.get("body_html"),
            "handle": data.get("handle"),
            "vendor": data.get("vendor"),
            "product_type": data.get("product_type"),
            "status": data.get("status"),
            "published_scope": data.get("published_scope"),
            "tags": data.get("tags"),
            "created_at": parse_datetime(data.get("created_at")),
            "updated_at": parse_datetime(data.get("updated_at")),
            "published_at": parse_datetime(data.get("published_at")),
            "raw_data": data,
        }
    )

    # Variants
    for v in data.get("variants", []):
        Variant.objects.update_or_create(
            shopify_variant_id=v["id"],
            defaults={
                "product": product,
                "title": v.get("title"),
                "price": v.get("price") or 0,
                "compare_at_price": v.get("compare_at_price"),
                "sku": v.get("sku"),
                "barcode": v.get("barcode"),
                "inventory_quantity": v.get("inventory_quantity", 0),
                "inventory_item_id": v.get("inventory_item_id"),
                "taxable": v.get("taxable", True),
                "position": v.get("position"),
                "created_at": parse_datetime(v.get("created_at")),
                "updated_at": parse_datetime(v.get("updated_at")),
            }
        )

    #  Options
    for o in data.get("options", []):
        Option.objects.update_or_create(
            product=product,
            name=o.get("name"),
            defaults={
                "position": o.get("position"),
                "values": o.get("values"),
            }
        )

    return product

from .models import Product


def delete_product(data):
    product_id = data.get("id")

    if not product_id:
        return False, "Missing product ID"

    try:
        product = Product.objects.get(shopify_id=product_id)
        product.delete()

        return True, "Deleted successfully"

    except Product.DoesNotExist:
        return False, "Product not found"