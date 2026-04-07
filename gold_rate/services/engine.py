import requests
from .shopify import  get_products , update_price
from .pricing import get_configs , calculate_price

def update_all_prices():
    config = get_configs()
    products = get_products()

    for product in products:
        for variant in product.get("variants", []):
            weight = variant.get("weight", 0) or 10

            purity = "22K" 

            gold_rate = config.get(purity, config["22K"])

            new_price = calculate_price(
                weight,
                gold_rate,
                config["making"],
                config["gst"]
            )

            print("🔥 Updating:", variant["id"], "→", new_price)

            update_price(variant["id"], new_price)