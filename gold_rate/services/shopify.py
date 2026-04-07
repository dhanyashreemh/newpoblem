import requests
from newone.settings import SHOP_URL, ACCESS_TOKEN

def get_products():
    print("🔥 SHOP_URL:", SHOP_URL)
    print("🔥 ACCESS_TOKEN:", ACCESS_TOKEN)
    url = f"{SHOP_URL}/admin/api/2024-01/products.json"
    headers = {"X-Shopify-Access-Token": ACCESS_TOKEN}

    print("🔥 FINAL URL:", url)

    res = requests.get(url, headers=headers)

    print("🔥 STATUS:", res.status_code)
    print("🔥 RESPONSE:", res.text)

    if res.status_code != 200:
        print("Failed to fetch products:", res.text)
        return []

    return res.json().get("products", [])


def get_metafields(product_id):
    url = f"{SHOP_URL}/admin/api/2024-01/products/{product_id}/metafields.json"
    headers = {"X-Shopify-Access-Token": ACCESS_TOKEN}

    res = requests.get(url, headers=headers)

    data = res.json().get("metafields", [])

    weight, purity = 0, "22K"

    for field in data:
        if field.get("key") == "weight":
            weight = float(field.get("value", 0))
        elif field.get("key") == "purity":
            purity = field.get("value")

    return weight, purity

def update_price(variant_id, new_price):
    url = f"{SHOP_URL}/admin/api/2024-01/variants/{variant_id}.json"

    headers = {
        "X-Shopify-Access-Token": ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "variant": {
            "id": variant_id,
            "price": str(new_price)
        }
    }

    res = requests.put(url, json=payload, headers=headers)

    if res.status_code != 200:
        print(f"Failed to update variant {variant_id}: {res.text}")
    else:
        print(f"Updated variant {variant_id} → ₹{new_price}")