from django.contrib import admin
from django.urls import path

from products.views import shopify_product_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/', shopify_product_webhook),
]
