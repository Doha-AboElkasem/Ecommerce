from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from cart.cart import Cart
from .serializers import OrderCreateSerializer
from .models import OrderItem


class CheckOutAPIView(APIView):
    def post(self, request):
        cart = Cart(request)

        if len(cart) == 0:
            return Response(
                {"error": "Cart is empty"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = OrderCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                order = serializer.save(
                    coupon=cart.coupon,
                    discount=cart.get_discount()
                )

                for item in cart:
                    product = item['product']

                    if product.stock < item['quantity']:
                        raise Exception(
                            f"Not enough stock for {product.name}. Available: {product.stock}"
                        )

                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        price=product.price,
                        quantity=item['quantity']
                    )

                    product.stock -= item['quantity']
                    product.save()

                cart.clear()

                return Response(
                    {
                        "message": "Order placed successfully",
                        "order_id": order.id
                    },
                    status=status.HTTP_201_CREATED
                )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
