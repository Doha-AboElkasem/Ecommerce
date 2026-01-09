from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone

from products.models import Product
from .cart import Cart
from .serializers import ProductCartSerializer
from .models import Coupon


class CartAPIView(APIView):

    def get(self, request):
        cart = Cart(request)
        items = []

        for item in cart:
            product = item['product']
            items.append({
                'product': ProductCartSerializer(product).data,
                'quantity': item['quantity'],
                'price': float(item['price']),
                'total_price': float(item['total_price']),
            })

        return Response({
            'items': items,
            'total_cart_price': float(cart.get_total_price()),
            'discount_amount': float(cart.get_discount()),
            'final_price': float(cart.get_total_price_after_discount()),
            'total_items': len(cart),
            'has_coupon': bool(cart.coupon),
            'coupon_code': cart.coupon.code if cart.coupon else None
        })

    def post(self, request):
        cart = Cart(request)
        action = request.data.get('action')

        if action == 'add':
            product_id = request.data.get('product_id')
            quantity = int(request.data.get('quantity', 1))

            product = get_object_or_404(Product, id=product_id)
            cart.add(product=product, quantity=quantity)

            return Response({'message': 'Product added to cart'})

        if action == 'apply_coupon':
            code = request.data.get('code')
            now = timezone.now()

            try:
                coupon = Coupon.objects.get(
                    code__iexact=code,
                    valid_from__lte=now,
                    valid_to__gte=now,
                    active=True
                )
                request.session['coupon_id'] = coupon.id
                request.session.modified = True

                return Response({'message': 'Coupon applied successfully'})
            except Coupon.DoesNotExist:
                return Response(
                    {'error': 'Invalid or expired coupon'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        return Response(
            {'error': 'Invalid action'},
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request):
        cart = Cart(request)
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=quantity, override_quantity=True)

        return Response({'message': 'Cart updated'})

    def delete(self, request):
        cart = Cart(request)
        action = request.data.get('action')

        if action == 'remove_product':
            product_id = request.data.get('product_id')
            product = get_object_or_404(Product, id=product_id)
            cart.remove(product)
            return Response({'message': 'Product removed from cart'})

        if action == 'remove_coupon':
            request.session['coupon_id'] = None
            request.session.modified = True
            return Response({'message': 'Coupon removed'})

        return Response(
            {'error': 'Invalid action'},
            status=status.HTTP_400_BAD_REQUEST
        )

class CouponAPIView(APIView):


    def post(self, request):
        code = request.data.get('code')
        now = timezone.now()

        if not code:
            return Response(
                {'error': 'Coupon code is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True
            )
            request.session['coupon_id'] = coupon.id
            request.session.modified = True

            return Response({'message': 'Coupon applied successfully'})
        except Coupon.DoesNotExist:
            return Response(
                {'error': 'Invalid or expired coupon'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request):
        request.session['coupon_id'] = None
        request.session.modified = True

        return Response({'message': 'Coupon removed'})
