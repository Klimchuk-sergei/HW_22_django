import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Очищает базу данных и заполняет ее данными из фикстур'

    @staticmethod
    def json_read_categories():
        with open('catalog/fixtures/categories.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('catalog/fixtures/products.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):
        # Очистка базы данных
        self.stdout.write(self.style.WARNING('Очистка базы данных...'))
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('База данных успешно очищена.'))

        # Списки для создания объектов
        categories_for_create = []
        products_for_create = []

        # Загрузка и подготовка категорий
        categories_data = self.json_read_categories()
        for category_item in categories_data:
            categories_for_create.append(
                Category(pk=category_item['pk'], **category_item['fields'])
            )
        Category.objects.bulk_create(categories_for_create)
        self.stdout.write(self.style.SUCCESS('Категории успешно загружены.'))

        # Загрузка и подготовка продуктов
        products_data = self.json_read_products()
        for product_item in products_data:
            # Получаем категорию по ID из уже созданных
            category = Category.objects.get(pk=product_item['fields']['category'])
            product_item['fields']['category'] = category

            # Создаем объект Product. Django сам добавит created_at и updated_at
            products_for_create.append(
                Product(pk=product_item['pk'], **product_item['fields'])
            )
        Product.objects.bulk_create(products_for_create)
        self.stdout.write(self.style.SUCCESS('Продукты успешно загружены.'))