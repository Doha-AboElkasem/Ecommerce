from django.urls import path
from .views import ProductDetailAPIView
urlpatterns = [
    path('api/product/<slug:slug>/', ProductDetailAPIView.as_view()),
]