from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    """
    Контроллер для отображения списка всех продуктов (Главная страница).
    """
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для отображения детальной информации о продукте.
    """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания нового продукта.
    """
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для редактирования существующего продукта.
    """
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления продукта.
    """
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
