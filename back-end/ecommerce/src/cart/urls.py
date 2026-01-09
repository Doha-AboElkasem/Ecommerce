
from django.urls import path
from .views import CartAPIView, CouponAPIView

urlpatterns = [
    path('cart/', CartAPIView.as_view(), name='cart-api'),
    path('coupon/apply/', CouponAPIView.as_view(), name='apply_coupon'),
]