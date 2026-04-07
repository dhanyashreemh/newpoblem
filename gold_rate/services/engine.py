import requests
from .shopify import get_metafields, get_products , update_price
from .pricing import get_configs , calculate_price

def update_all_prices():
    config = get_configs()
    products = get_products()

    for product in products:
        product_id = product.get("id")

        weight, purity = get_metafields(product_id)

        if weight == 0:
            continue

        gold_rate = config.get(purity, config["22K"])

        for variant in product.get("variants", []):
            new_price = calculate_price(
                weight,
                gold_rate,
                config["making"],
                config["gst"]
            )

            update_price(variant["id"], new_price)