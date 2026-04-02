from django.contrib import admin
from django.urls import path

from products.views import shopify_product_webhook, force_migrate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/', shopify_product_webhook),
    path('force-migrate/', force_migrate)
]
