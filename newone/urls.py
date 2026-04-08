from django.contrib import admin
from django.urls import path
from gold_rate.views import get_gold_rate, update_gold_rate
from products.views import shopify_product_delete_webhook, shopify_product_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/product/CreateUpdate/', shopify_product_webhook),
    path("webhook/product/delete/", shopify_product_delete_webhook),
    path('gold-rate/', get_gold_rate),
    path("update-gold-rate/", update_gold_rate),
]
