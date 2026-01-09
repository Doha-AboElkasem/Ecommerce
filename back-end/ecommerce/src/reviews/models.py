from django.db import models
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_avatar = models.ImageField(upload_to='media/testimonials/')
    client_review = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.client_name}"
    
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField()
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.product.name} ({self.rating} Stars)"