from .models import Product, Category
from django.core.cache import cache
from django.conf import settings


def get_products_by_category(category_pk):
    if category_pk is None:
        return Product.objects.none()
    return Product.objects.filter(category__id=category_pk)

def get_cached_categories():
    if settings.CACHE_ENABLED:
        category_list = cache.get('category_list')
        if category_list is None:
            category_list = Category.objects.all()
            cache.set('category_list', category_list, 3600)
    else:
        category_list = Category.objects.all()
    return category_list