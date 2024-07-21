from django.db import models


class Customer(models.Model):
    CUSTOMER_TYPE_CHOICES = [
        ('Individual', 'Individual'),
        ('Corporate', 'Corporate'),
        ('Business', 'Business'),
        ('Government', 'Government'),
        ('Organization', 'Organization'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=100,)
    address = models.CharField(max_length=200, )
    phone = models.CharField(max_length=20, )
    email = models.EmailField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=CUSTOMER_TYPE_CHOICES, default='individual',)
    district = models.CharField(max_length=100, )
    subdistrict = models.CharField(max_length=100, )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
    def __str__(self):
        return f"{self.name} ({self.phone}) - {self.type}"

