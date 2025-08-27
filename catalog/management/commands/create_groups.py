from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу модераторов с необходимыми правами'

    def handle(self, *args, **options):
        # Создаем или получаем группу
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана.'))
        else:
            self.stdout.write(self.style.WARNING('Группа "Модератор продуктов" уже существует.'))

        # Получаем content type для модели Product
        product_content_type = ContentType.objects.get_for_model(Product)

        # Получаем необходимые права
        can_unpublish = Permission.objects.get(
            codename='can_unpublish_product',
            content_type=product_content_type,
        )
        delete_product = Permission.objects.get(
            codename='delete_product',
            content_type=product_content_type,
        )

        # Добавляем права в группу
        moderator_group.permissions.add(can_unpublish, delete_product)
        self.stdout.write(self.style.SUCCESS('Права успешно добавлены в группу.'))