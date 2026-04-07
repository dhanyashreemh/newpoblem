from django.http import JsonResponse
from .models import GoldRate
from .services.engine import update_all_prices
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import requests

@csrf_exempt
@api_view(["GET"])
def get_gold_rate(request):
    if request.method != "GET":
        return JsonResponse({"error": "Only GET allowed"}, status=405)

    purity = request.GET.get("purity", "22K")

    valid_purities = ["22K", "24K"]

    if purity not in valid_purities:
        return JsonResponse({"error": "Invalid purity"}, status=400)

    rate = GoldRate.objects.filter(purity=purity).order_by("-updated_at").first()

    if not rate:
        return JsonResponse({"error": f"No {purity} rate found"}, status=400)

    return JsonResponse({
        "purity": purity,
        "rate": rate.rate_per_gram
    })


@csrf_exempt
@api_view(["POST"])
def update_gold_rate(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body)

        rate = data.get("rate")
        purity = data.get("purity")

        if rate is None or purity is None:
            return JsonResponse({"error": "rate and purity required"}, status=400)

        if purity not in ["22K", "24K"]:
            return JsonResponse({"error": "Invalid purity"}, status=400)

        GoldRate.objects.create(
            purity=purity,
            rate_per_gram=rate
        )

        update_all_prices()

        return JsonResponse({"status": "Prices Updated"})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    


