from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
import hmac, hashlib, base64
from .services import create_or_update_product
from django.core.management import call_command
import logging

logger = logging.getLogger(__name__)


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
    webhook_id = request.headers.get("X-Shopify-Webhook-Id")

    logger.info(f"Webhook received: {webhook_id}")

    # ✅ Security check
    if not verify_webhook(request):
        logger.warning("Unauthorized webhook attempt")
        return Response({"error": "Unauthorized"}, status=401)

    data = request.data
    print("parsed data" , data)

    try:
        product , error = create_or_update_product(data)
        if product:
            return Response({"message": "Success"}, status=200)
        else:
            return Response({"error": error}, status=400)
        
    except Exception as e:
        logger.error(f"Webhook failed: {str(e)}")
        return Response({"error": "Internal Server Error"}, status=500)
    
from .services import delete_product

@api_view(["POST"])
def shopify_product_delete_webhook(request):
    if not verify_webhook(request):
        return Response({"error": "Unauthorized"}, status=401)

    data = request.data

    success, message = delete_product(data)

    if success:
        return Response({"message": message}, status=200)
    else:
        return Response({"error": message}, status=400)

@api_view(["GET"])
def force_migrate(request):
    # Step 1: Reset migration history WITHOUT touching DB
    call_command('migrate', 'products', 'zero', fake=True)

    # Step 2: Apply migrations properly (creates tables)
    call_command('migrate')

    return Response({"status": "migrations fixed"})