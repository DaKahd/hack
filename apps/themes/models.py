from django.db import models
from django.forms import ValidationError
from django.utils.text import slugify


class BaseTheme(models.Model):
    
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
    is_active = models.BooleanField(
        blank=False,
        null=False,
        help_text="Select this if you want item to be displayed on website",
        default=False
    )

    def __str__(self):

        return self.title

    
class ParentTheme(BaseTheme):

    class Meta:
        verbose_name = "Parent Theme"
        verbose_name_plural = 'Parent Themes'


class ChildTheme(BaseTheme):

    parent_theme = models.ForeignKey(
        ParentTheme, 
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Example: Winter child theme would go into seasonal parent theme"
    )

    slug = models.SlugField(
        max_length=50,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Child Theme"
        verbose_name_plural = 'Child Themes'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def clean(self):
        if not self.is_active:
            raise ValidationError(
                "is active must be set to true to make theme live"
                )
