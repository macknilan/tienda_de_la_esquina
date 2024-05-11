""" MODEL PRODUCTS """

from django.db import models
from django.utils.translation import gettext_lazy as _

# Utilities
from apps.utils.models import TimeStampedModel


class Product(TimeStampedModel):
    """
    PRODUCT MODEL.
    A PRODUCT IS A ITEM THAT CAN BE SOLD.
    """
    name = models.CharField(_("name"), max_length=100)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)  # 999999.99
    sku = models.CharField(_("stock keeping unit"), max_length=50, unique=True)
    category = models.CharField(_("category"), max_length=50)
    image = models.ImageField(_("image"), upload_to="media/products", blank=True, null=True)
    discount = models.DecimalField(_("discount"), max_digits=5, decimal_places=2, default=0.00)  # 100.00
    brand = models.CharField(_("brand"), max_length=50)

    class Meta(TimeStampedModel.Meta):
        """OVERWRITE META CLASS OF TimeStampedModel"""

        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ["-created_at"]
        db_table = "products"

    def __str__(self):
        return f"{self.name} | {self.brand}"
