from django.contrib import admin

from .models import Category, Blog


class BlogAdmin(admin.ModelAdmin):    # Відповідає за формування slug (test-blog-about-football)
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_display = ('title', 'category', 'author', 'status', 'is_featured')    # Створюємо заголовки в адмін-панелі
    search_fields = ('id', 'title', 'category__category_name', 'status')    # Дає можливість пошуку в адімн-панелі
    list_editable = ('is_featured',)    # Дає можливість ставити галочку в стовпці IS FEATURED безпосередньо в меню адмін-панелі, також появилась кнопка SAVE


# Register your models here.

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
