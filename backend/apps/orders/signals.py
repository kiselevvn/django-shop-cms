# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from .models import Order
# from .service import OrderToWarehouse


# @receiver(post_save, sender=Order)
# def order_to_warehouse(sender, instance, created, **kwargs):
#     if created:
#         service = OrderToWarehouse()
#         service.execute(instance)
