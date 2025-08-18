from django import forms
from .models import Product

# Список запрещенных слов
FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """
        Метод для стилизации формы.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Добавляем класс 'form-control' ко всем полям
            field.widget.attrs['class'] = 'form-control'

            # Особая стилизация для чекбокса
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price',)

    def clean_name(self):
        """
        Валидация поля 'name' на наличие запрещенных слов.
        """
        cleaned_data = self.cleaned_data['name'].lower()
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError(f"Слово '{word}' запрещено к использованию в названии.")
        return cleaned_data

    def clean_description(self):
        """
        Валидация поля 'description' на наличие запрещенных слов.
        """
        cleaned_data = self.cleaned_data['description'].lower()
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError(f"Слово '{word}' запрещено к использованию в описании.")
        return cleaned_data

    def clean_price(self):
        """
        Валидация поля 'price'. Проверяет, что цена не отрицательная.
        """
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price