from django.contrib import admin


from apps.products.models import Product, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    PRODUCT ADMIN.
    """
    list_display = ["name", "brand", "price", "sku", "category", "discount"]
    list_filter = ["category", "brand"]
    search_fields = ["name", "sku", "brand"]
    list_per_page = 100
    fieldsets = (
        ("PRODUCT INFO", {
            "fields": ("name", "brand", "description", "price", "sku", "category", "image")
        }),
        ("DISCOUNT", {
            "fields": ("discount",)
        }),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    BRAND ADMIN.
    """
    list_display = ["name", "description"]
    search_fields = ["name"]
    list_per_page = 50
    fieldsets = (
        ("BRAND INFO", {
            "fields": ("name", "description", "logo")
        }),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
