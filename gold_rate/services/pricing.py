import requests
from newone.settings import SHOP_URL, ACCESS_TOKEN


def get_configs():
    from gold_rate.models import PricingConfig 
    config = PricingConfig.objects.first()

    if not config:
        raise Exception("Missing configuration")

    return {
        "22K": config.gold_22k,
        "24K": config.gold_24k,
        "gst": config.gst_percent,
        "making": config.making_charge
    }

def calculate_price(weight, gold_rate, making_charge, gst):
    base = (weight * gold_rate) + (weight * making_charge)
    return round(base * (1 + gst / 100), 2)
