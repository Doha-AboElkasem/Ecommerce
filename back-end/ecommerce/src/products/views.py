from django.shortcuts import get_object_or_404, render
from .models import Product, Category
from .serializers import ProductDetailSerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

#Product detail Page View
class ProductDetailAPIView(APIView):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug, available=True)
        product.views += 1
        product.save()
        
        serializer = ProductDetailSerializer(product)
        
        related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
        related_serializer = ProductSerializer(related_products, many=True)
        
        return Response({
            'product': serializer.data,
            'related_products': related_serializer.data
        })