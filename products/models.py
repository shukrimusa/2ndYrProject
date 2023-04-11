from django.db import models
import uuid
from django.urls import reverse


# Category Table

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to='category', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("products:products_by_category", args=[self.id])

    def __str__(self):
        return self.name


# Product Table

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product', blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_absolute_url(self):
        return reverse("products:product_detail", args=[self.category.id, self.id])

    def __str__(self):
        return self.title
