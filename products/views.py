from django.shortcuts import render
import hmac
import hashlib
import base64
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import hmac, hashlib, base64
from .services import create_or_update_product
from django.core.management import call_command

def verify_webhook(request):
    received_hmac = request.headers.get("X-Shopify-Hmac-Sha256")

    if not received_hmac:
        return False

    secret = settings.SHOPIFY_WEBHOOK_SECRET.encode("utf-8")
    body = request.body

    computed_hmac = base64.b64encode(
        hmac.new(secret, body, hashlib.sha256).digest()
    ).decode()

    return hmac.compare_digest(received_hmac, computed_hmac)

@api_view(["POST"])
def shopify_product_webhook(request):

    print("🔥 WEBHOOK HIT")
    print("Headers:", request.headers)
    print("Body:", request.body)

    # ✅ verify webhook properly
    if not verify_webhook(request):
        return Response({"error": "Unauthorized"}, status=401)

    data = request.data
    print("Parsed Data:", data)

    try:
        create_or_update_product(data)
        return Response({"message": "Success"}, status=200)

    except Exception as e:
        print("ERROR:", str(e))
        return Response({"error": str(e)}, status=500)

@api_view(["GET"])
def force_migrate(request):
    call_command('migrate', 'products', 'zero')
    call_command('migrate')
    return Response({"status": "migrations reapplied"})