from django.urls import path
from .views import HomePageView, ContactView, ShopView
urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('contact/', ContactView.as_view(), name='contact'),
]