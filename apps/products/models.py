from django.db import models
from apps.themes.models import ChildTheme

class Product(models.Model):

    title = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    desciption = models.CharField(
        max_length=750,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='product/images',
        blank=False,
        null=False
    )

    