from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail(request, pk):
    """контролер для страниц с информацией о товаре"""
    product_item = get_object_or_404(Product, pk=pk)

    context = {
        'product': product_item,
        'title': product_item.name
    }
    return render(request, 'catalog/product_detail.html', context)


def home(request):
    """
    Контроллер для главной страницы.
    Получает все продукты и передает их в шаблон.
    """
    product_list = Product.objects.all()
    context = {
        'products': product_list,
        'title': 'Главная страница'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"Новое сообщение от пользователя {name} (телефон: {phone}): {message}")

        context = {
            'success': True
        }

        return render(request, 'contacts.html', context)

    return render(request, 'contacts.html')
