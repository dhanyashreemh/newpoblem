import requests
from newone.settings import SHOP_URL, ACCESS_TOKEN
from gold_rate.models import GoldRate , TaxConfig, MakingCharges


def get_configs():
    gold_22k = GoldRate.objects.filter(purity="22K").last()
    gold_24k = GoldRate.objects.filter(purity="24K").last()
    tax = TaxConfig.objects.first()
    making = MakingCharges.objects.first()

    if not all([gold_22k, gold_24k, tax, making]):
        raise Exception(" Missing configuration")

    return {
        "22K": gold_22k.rate_per_gram,
        "24K": gold_24k.rate_per_gram,
        "gst": tax.gst_percent,
        "making": making.charge_per_gram
    }


def calculate_price(weight, gold_rate, making_charge, gst):
    base = (weight * gold_rate) + (weight * making_charge)
    return round(base * (1 + gst / 100), 2)
