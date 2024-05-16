""" MODEL PRODUCTS """

from django.db import models
from django.utils.translation import gettext_lazy as _
from nanoid import generate

# Utilities
from apps.utils.models import TimeStampedModel

# Models
from .brands import Brand


class Product(TimeStampedModel):
    """
    PRODUCT MODEL.
    A PRODUCT IS A ITEM THAT CAN BE SOLD.
    """
    id = models.AutoField(
        db_column="product_id",
        primary_key=True,
    )
    name = models.CharField(_("name"), help_text="Name of the product", max_length=100)
    price = models.DecimalField(_("price"), help_text="Price of the product", max_digits=10, decimal_places=2)  # 999999.99
    sku = models.CharField(_("SKU"), help_text="Unique ID", max_length=50, unique=True)
    category = models.CharField(_("category"), help_text="Category", max_length=50)
    image = models.ImageField(_("image"), help_text="Picture of product", upload_to="media/products", blank=True, null=True)
    discount = models.DecimalField(_("discount"), help_text="Discount", max_digits=5, decimal_places=2, default=0.00)  # 100.00
    description = models.TextField(_("description"), help_text="Good description", max_length="500", blank=True, null=True)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("brand of the product"),
    )

    class Meta(TimeStampedModel.Meta):
        """OVERWRITE META CLASS OF TimeStampedModel"""

        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ["-created_at"]
        db_table = "product_info"

    def __str__(self):
        return f"{self.name} | {self.brand}"



