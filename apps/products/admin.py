from django.contrib import admin


from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    PRODUCT ADMIN.
    """
    list_display = ["name", "brand", "price", "sku", "category", "discount"]
    list_filter = ["category", "brand"]
    search_fields = ["name", "sku", "brand"]
    list_per_page = 10
    fieldsets = (
        ("PRODUCT INFO", {
            "fields": ("name", "brand", "price", "sku", "category", "image")
        }),
        ("DISCOUNT", {
            "fields": ("discount",)
        }),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]

