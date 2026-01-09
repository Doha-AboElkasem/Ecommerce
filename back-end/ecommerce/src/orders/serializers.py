from rest_framework import serializers
from .models import Order
class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'company_name', 'country', 
            'address_1', 'address_2', 'city', 'state', 'zip_code', 
            'phone', 'email', 'additional_info'
        ]