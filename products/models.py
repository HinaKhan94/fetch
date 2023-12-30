from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True,
        blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2, null=True,
        blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """ Model for Reviews """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="reviews",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviews"
    )
    created_on = models.DateField(
        auto_now_add=True,
        blank=False,
        null=False
    )
    content = models.TextField(
        max_length=500
    )
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5, message="Must be between 0-5"),
            MinValueValidator(0, message="Must be between 0-5")
        ],
        default=0,
        blank=False,
        null=False
    )

    is_approved = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.user}"
