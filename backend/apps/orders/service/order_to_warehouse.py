from apps.warehouse.models import OperationPosition, Operation


class OrderToWarehouse:
    """
    Order to Warehouse
    """

    def create_warehouse_positions(
        self,
        order,
        operation,
    ):
        """
        Order position to
        warehouse operation positions
        """
        operation_positions = []
        for position in order.positions.all():
            operation_positions.append(
                OperationPosition(
                    operation=operation,
                    product=position.product,
                    count=-position.count,
                )
            )
        position.count = -position.count
        return operation_positions

    def execute(self, order_instance, user_instance):
        """ Main service function """

        # create operation
        operation = Operation.objects.create(
            comment=order_instance.comment, user=user_instance
        )

        # create operation in database
        # operation.save()

        # create positions list
        positions = self.create_warehouse_positions(order_instance, operation)

        # create positions in database
        OperationPosition.objects.bulk_create(positions)
