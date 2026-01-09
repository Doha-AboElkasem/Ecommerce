from rest_framework import serializers
from products.models import Product

class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image'] 
        