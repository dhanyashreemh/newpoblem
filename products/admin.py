from django.contrib import admin
from .models import Product, Variant, Option, ProductImage


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 0


class OptionInline(admin.TabularInline):
    model = Option
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "vendor", "product_type", "status"]
    search_fields = ["title", "vendor"]

    # 🔥 EVERYTHING in one place
    inlines = [VariantInline, OptionInline, ProductImageInline]