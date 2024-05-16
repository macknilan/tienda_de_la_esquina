""" MODEL BRANDS """

from django.db import models
from django.utils.translation import gettext_lazy as _

# Utilities
from apps.utils.models import TimeStampedModel


class Brand(TimeStampedModel):
    """
    BRAND MODEL.
    A BRAND IS A NAME, TERM, DESIGN, SYMBOL, OR ANY OTHER FEATURE THAT IDENTIFIES ONE SELLER'S
    GOOD OR SERVICE AS DISTINCT FROM THOSE OF OTHER SELLERS.
    """
    id = models.AutoField(
        db_column="brand_id",
        primary_key=True,
    )
    name = models.CharField(_("name"), max_length=50, unique=True)
    description = models.TextField(_("description"), blank=True, null=True)
    logo = models.ImageField(_("logo"), upload_to="media/brands", blank=True, null=True)

    class Meta(TimeStampedModel.Meta):
        """OVERWRITE META CLASS OF TimeStampedModel"""

        verbose_name = _("brand")
        verbose_name_plural = _("brands")
        ordering = ["-created_at"]
        db_table = "brand_info"

    def __str__(self):
        return self.name
