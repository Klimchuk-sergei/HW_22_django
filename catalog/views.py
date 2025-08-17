from django.views.generic import ListView, DetailView, TemplateView
from .models import Product


class ProductListView(ListView):
    """
    Контроллер для отображения списка всех продуктов (Главная страница).
    """
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        # Добавляем title в контекст для базового шаблона
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class ProductDetailView(DetailView):
    """
    Контроллер для отображения детальной информации о продукте.
    """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        # Добавляем title в контекст, используя имя продукта
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class ContactsView(TemplateView):
    """
    Контроллер для страницы контактов.
    """
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Новое сообщение от {name} (телефон: {phone}): {message}")

        context = self.get_context_data()
        context['success'] = True
        return self.render_to_response(context)