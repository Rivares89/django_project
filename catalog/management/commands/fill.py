from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {'name': 'Смартфоны',
             'description': 'мобильный телефон (современный — как правило, с сенсорным экраном)',#, дополненный функциональностью умного устройства',
             'category': 'Смартфоны и гаджеты',
             'price_for_one': '10000',
             'date_creation': '25.12.2023',
             'last_modified_data': '25.12.2023'},
            {'name': 'Планшеты',
             'description': 'электронное устройство с сенсорным экраном, позволяющее управлятькомпьютернымипрограммами', # с помощью прикосновений пальцев к объектам на экране',
             'category': 'Смартфоны и гаджеты',
             'price_for_one': '15000',
             'date_creation': '25.12.2023',
             'last_modified_data': '25.12.2023'},
            {'name': 'Сотовые телефоны',
             'description': 'телефон, предназначенный для работы в сетях сотовой связи',
             'category': 'Смартфоны и гаджеты',
             'price_for_one': '5000',
             'date_creation': '25.12.2023',
             'last_modified_data': '25.12.2023'},
            {'name': 'Электронные книги',
             'description': 'компактное планшетное компьютерное устройство, предназначенное для отображения текста',# в электронном виде',
             'category': 'Смартфоны и гаджеты',
             'price_for_one': '7000',
             'date_creation': '25.12.2023',
             'last_modified_data': '25.12.2023'},
            {'name': 'Смарт-часы',
             'description': 'компьютеризированные наручные часы с расширенной функциональностью',
             'category': 'Смартфоны и гаджеты',
             'price_for_one': '8000',
             'date_creation': '25.12.2023',
             'last_modified_data': '25.12.2023'},
            {'name': 'Моноблоки',
             'description': 'персональный компьютер, все устройства которого, за исключением клавиатуры, мыши',# и иногда блока питания, заключены в один корпус вместе с монитором',
             'category': 'Компьютеры и моноблоки',
             'price_for_one': '30000',
             'date_creation': '25.12.2023',
             'last_modified_data': '25.12.2023'},
            {'name': 'Ноутбуки',
             'description': 'переносной компьютер, в корпусе которого объединены типичные компоненты ПК',#, включая дисплей, клавиатуру и устройство указания (обычно сенсорная панель или тачпад), а также аккумуляторные батареи.',
             'category': 'Компьютеры и моноблоки',
             'price_for_one': '40000',
             'date_creation': '25.12.2023',
             'last_modified_data': '25.12.2023'},
            {'name': 'Мониторы',
             'description': 'устройство оперативной визуальной связи пользователя с управляющим устройством',# и отображением данных, передаваемых с клавиатуры, мыши или центрального процессора',
             'category': 'Компьютеры и моноблоки',
             'price_for_one': '25000',
             'date_creation': '25.12.2023',
             'last_modified_data': '25.12.2023'},
        ]

        product_for_create = []
        for item in product_list:
            product_for_create.append(
                Product(**item)
            )

        Product.objects.bulk_create(product_for_create)
