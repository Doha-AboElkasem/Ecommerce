from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/categories/%Y/%m/%d/', null=True, blank=True)
    slug = models.SlugField(unique=True)
    class Meta:
        verbose_name_plural = 'Categories'
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='media/products/%Y/%m/%d/', null=True, blank=True)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True)
    sales_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.name
