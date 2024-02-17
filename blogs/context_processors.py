from .models import Category


def get_categories(request):    # Виводить список категорій на кожній сторінці
    categories = Category.objects.all()
    return dict(categories=categories)