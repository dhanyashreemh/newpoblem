from django.http import JsonResponse
from .models import PricingConfig
from .services.engine import update_all_prices
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import PricingConfig

@csrf_exempt
def shopify_product_update(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # DEBUG FIRST (IMPORTANT)
        print("SHOPIFY WEBHOOK DATA:", data)

        # OPTION 1: Using price
        for variant in data.get("variants", []):
            price = float(variant.get("price", 0))

            PricingConfig.objects.update_or_create(
                id=1,
                defaults={"gold_22k": price}
            )

        return JsonResponse({"status": "updated"})

@csrf_exempt
@api_view(["GET"])
def get_gold_rate(request):
    config = PricingConfig.objects.first()

    if not config:
        return JsonResponse({"error": "No pricing config found"}, status=400)

    return JsonResponse({
        "gold_22k": config.gold_22k,
        "gold_24k": config.gold_24k,
        "gst": config.gst_percent,
        "making": config.making_charge
    })


@csrf_exempt
@api_view(["POST"])
def update_gold_rate(request):
    try:
        data = json.loads(request.body)

        gold_22k = data.get("gold_22k")
        gold_24k = data.get("gold_24k")
        gst = data.get("gst")
        making = data.get("making")

        if None in [gold_22k, gold_24k, gst, making]:
            return JsonResponse({"error": "All fields required"}, status=400)

        PricingConfig.objects.update_or_create(
            id=1,
            defaults={
                "gold_22k": gold_22k,
                "gold_24k": gold_24k,
                "gst_percent": gst,
                "making_charge": making
            }
        )

        update_all_prices()

        return JsonResponse({"status": "Prices Updated"})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    

@csrf_exempt
def shopify_product_webhook(request):
    return JsonResponse({"status": "ok"})


@csrf_exempt
def shopify_product_update(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # DEBUG FIRST (IMPORTANT)
        print("SHOPIFY WEBHOOK DATA:", data)

        # OPTION 1: Using price
        for variant in data.get("variants", []):
            price = float(variant.get("price", 0))

            PricingConfig.objects.update_or_create(
                purity="22K",
                defaults={"rate": price}
            )

        return JsonResponse({"status": "updated"})