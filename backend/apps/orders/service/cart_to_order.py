from ..models import Order, OrderPosition


class CartToOrder:
    def execute(self, user, comment):
        order_positions = []
        order = Order.objects.create(comment=comment, user=user)

        for cart_position in user.products_in_cart.all():
            order_positions.append(
                OrderPosition(
                    order=order,
                    count=cart_position.count,
                    product=cart_position.product,
                )
            )

        OrderPosition.objects.bulk_create(order_positions)
        return order
