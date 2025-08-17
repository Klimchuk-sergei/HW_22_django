from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Настройки для отображения модели Blog в админ-панели.
    """

    list_display = ('id', 'title', 'is_published', 'views_count', 'created_at',)

    list_filter = ('is_published',)

    search_fields = ('title', 'content',)