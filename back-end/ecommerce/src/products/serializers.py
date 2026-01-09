from rest_framework import serializers
from .models import Category, Product
from reviews.models import ProductReview
from django.db.models import Avg
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image', 'slug', 'category']

#Product Detail Serializer
class ProductDetailSerializer(serializers.ModelSerializer):
    reviews_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'category', 'description', 'image', 
            'price', 'stock', 'available', 'slug', 
            'reviews_count', 'average_rating'
        ]

    def get_reviews_count(self, obj):
        return ProductReview.objects.filter(product=obj, is_active=True).count()

    def get_average_rating(self, obj):
        average = ProductReview.objects.filter(product=obj, is_active=True).aggregate(Avg('rating'))['rating__avg']
        return round(average, 1) if average else 0