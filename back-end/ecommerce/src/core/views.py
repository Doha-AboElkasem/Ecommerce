from django.shortcuts import render
from .serializers import ContactMessageSerializer
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from reviews.models import Testimonial
from reviews.serializers import TestimonialSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class HomePageView(APIView):
    def get(self, request):
        categories = Category.objects.filter()[:4]
        trending_products = Product.objects.filter(available=True).order_by('-views')[:3]
        popular_products = Product.objects.filter(available=True).order_by('-sales_count')[:3]
        customers_reviews = Testimonial.objects.all()
        data = {
            'trending_products': ProductSerializer(trending_products, many=True).data,
            'categories': CategorySerializer(categories, many=True).data,
            'popular_products': ProductSerializer(popular_products, many=True).data,
            'customers_reviews': TestimonialSerializer(customers_reviews, many=True).data,
        }

        return Response(data, status=status.HTTP_200_OK)
    

#Shop View
class ShopView(APIView):
    def get(self, request):
        products = Product.objects.filter(available=True)
        sort_by = request.query_params.get('sort_by')
        if sort_by == 'popularity':
            products = products.order_by('-sales_count')
        elif sort_by == 'average_rating':
            products = products.order_by('-rating')  
        elif sort_by == 'latest':
            products = products.order_by('-created_at')
        elif sort_by == 'price_low_to_high':
            products = products.order_by('price')
        elif sort_by == 'price_high_to_low':
            products = products.order_by('-price')
        else:
            products = products.order_by('-created_at')

        products = products[:6]

        serializer = ProductSerializer(products, many=True)
        data = {
            'products': ProductSerializer(products, many=True).data,
        }
        return Response(data, status=status.HTTP_200_OK)
    

#Contact View
class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Contact message sent successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)