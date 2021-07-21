from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify

from django.utils.translation import gettext as _


class Product(models.Model):
    """Product model implementation"""

    class Meta:
        db_table = "product"
        verbose_name = _("product")
        verbose_name_plural = _("products")

    brand = models.CharField(
        max_length=128,
        verbose_name=_("product brand title"),
        help_text=_("Required. 128 characters or fewer."),
    )

    product = models.CharField(
        max_length=128,
        verbose_name=_("product title"),
        help_text=_("Required. 128 characters or fewer."),
    )

    slug = models.SlugField(
        max_length=128,
        verbose_name=_("product slug"),
        help_text=_("Required. 128 characters or fewer. "
                    "Letters, numbers, hyphens and underscores."),
    )

    image = models.ImageField(
        upload_to="product",
        default="default/product.png",
    )

    description = models.TextField(
        verbose_name=_("product description and/or specifications"),
        help_text=_("Required")
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0.00)],
        verbose_name=_("price for a single item"),
        help_text=_("A positive decimal number. Defaults to numeric zero."),
    )

    quantity = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name=_("number of available items"),
        help_text=_("A positive integer number. Defaults to integer zero."),
    )

    def __repr__(self):
        """Return a string representation of an instance"""

        return f"<{self.__class__.__name__} pk={self.pk} ('{self}')>"

    def __str__(self):
        """Return a string version of an instance"""

        return self.product

    @property
    def name(self):
        """An alias to a product field"""

        return self.product

    def get_absolute_url(self):
        """Return an absolute URL to a product instance"""

        return reverse_lazy("store:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """Override save method"""

        if not self.slug:
            self.slug = slugify(self.product)

        super(Product, self).save(*args, **kwargs)
