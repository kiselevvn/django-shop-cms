from django.core.management.base import BaseCommand
from ...models import Product, Category


class Command(BaseCommand):
    help = "тестовые данные"

    def create_test_product(self):
        short_description = (
            "краткое описание тестового товара short_description " * 3
        )
        description = "Описание тестового товара description " * 7
        product = Product.objects.create(
            name="Тестовый товар №",
            is_published=True,
            price=100.50,
            short_description=short_description,
            description=description,
        )
        product.save()
        return product

    def handle(self, *args, **options):
        product = self.create_test_product()
        product.pk = None
        products = []
        for i in range(19):
            products.append(product)
        Product.objects.bulk_create(products)


