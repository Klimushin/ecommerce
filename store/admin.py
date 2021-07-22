from django.contrib import admin

from store.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin implementation"""

    fields = [
        "brand",
        "image",
        "slug",
        "product",
        "description",
        "price",
        "quantity",
    ]

    prepopulated_fields = {"slug": ["product"]}

    list_display = [
        "product",
        "brand",
        "price",
        "quantity",
    ]

    list_display_links = [
        "product",
    ]

    list_editable = [
        "price",
        "quantity",
    ]

    list_filter = ["brand"]
