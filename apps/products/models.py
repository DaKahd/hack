from django.db import models
from apps.themes.models import ChildTheme
from django.utils.text import slugify


class Product(models.Model):

    title = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    description = models.CharField(
        max_length=750,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='product/images',
        blank=False,
        null=False
    )

    is_active = models.BooleanField(
        blank=True,
        null=True,
        default=False
    )

    in_progress = models.BooleanField(
        blank=True,
        null=True,
        default=False
    )

    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=False,
        null=False,
        default=0.0
    )

    sale_price =  models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=False,
        null=False,
        default=0.0
    )

    quantity = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        default=0,
    )

    in_progress_quantity = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        default=0,
    )

    slug = models.SlugField(
        max_length=50,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)