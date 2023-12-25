from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {'name': 'Телевизор', 'category': 'TV'},
            {'name': 'Монитор', 'category': 'TV'},
            {'name': 'Телефон', 'category': 'Смартфоны'},
            {'name': 'Айфон', 'category': 'Смартфоны'},
        ]

        product_for_create = []
        for item in product_list:
            product_for_create.append(
                Product(**item)
            )

        Product.objects.bulk_create(product_for_create)

