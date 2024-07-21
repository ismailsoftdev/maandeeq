from django.db import models
from django.core.validators import MinValueValidator

class Brand(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_number = models.CharField(max_length=255, unique=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.product_number:
            last_product = Product.objects.order_by('-id').first()
            unique_id = f"{last_product.id + 1:06}{str(self.brand.code).zfill(6)}"
            self.product_number = unique_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand.name} - {self.name}"
