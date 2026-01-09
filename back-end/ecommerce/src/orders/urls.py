from django.urls import path
from .views import CheckOutAPIView
urlpatterns = [
    path('checkout/', CheckOutAPIView.as_view(), name='order-create'),
]