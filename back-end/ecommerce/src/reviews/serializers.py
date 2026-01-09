from rest_framework import serializers
from .models import ProductReview, Testimonial

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['product', 'rating', 'review_text', 'client_name', 'client_email']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'client_review', 'client_avatar']
