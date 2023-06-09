from django.db import models
from django.forms import ValidationError
from apps.themes.models import ChildTheme
from django.utils.text import slugify


class Product(models.Model):

    child_theme = models.ForeignKey(
        ChildTheme,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text="""If you make this a part of a child theme, 
        if the child theme is deleted so are the posts within it"""
    )

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
        blank=True,
        null=True,
        default=0.0
    )

    sale = models.BooleanField(
        default=False,
        blank=True,
        null=True
    )

    quantity = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
        default=0,
    )



    slug = models.SlugField(
        max_length=50,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('price',)
        verbose_name = "Product"
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if self.sale_price:
                self.sale = True
        super().save(*args, **kwargs)
        

    def clean(self):
        if self.is_active and self.in_progress:
            raise ValidationError("Item cannot be active and in progress at the same time")

       