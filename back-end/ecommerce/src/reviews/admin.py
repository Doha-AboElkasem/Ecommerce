from django.contrib import admin

# Register your models here.
from .models import Testimonial, ProductReview

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('client_name', 'content')
    ordering = ('-created_at',)

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'product', 'rating', 'is_active', 'created_at')
    list_filter = ('is_active', 'rating', 'created_at')
    search_fields = ('client_name', 'client_email', 'review_text', 'product__name')
    ordering = ('-created_at',)
