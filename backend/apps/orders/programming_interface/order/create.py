from rest_framework.generics import CreateAPIView
from rest_framework.serializers import ModelSerializer
from ...models import Order
from ...service import OrderToWarehouse, CartToOrder


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "comment",
        ]

    def create(self, validated_data):

        comment = validated_data.pop("comment")

        user = self.context["request"].user
        if len(user.products_in_cart.all()) > 0:
            #
            service_cart_to_order = CartToOrder()
            order = service_cart_to_order.execute(user=user, comment=comment)
            #
            service_order_to_warehouse = OrderToWarehouse()
            service_order_to_warehouse.execute(order, user)
            #
            user.products_in_cart.all().delete()
            #
            return order
        return Order()


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
