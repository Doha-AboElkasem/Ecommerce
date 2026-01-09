from django.db import models
from products.models import Product
from cart.models import Coupon
from django.contrib.auth.models import User

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=250) 
    address_2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=100) 
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0)
    additional_info = models.TextField(blank=True)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)