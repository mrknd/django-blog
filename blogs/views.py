from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Blog, Category


# Create your views here.
def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category
    posts = Blog.objects.filter(status='Published', category=category_id)
    # Use try/except when we want to do some custom action if the category does not exist
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # Redirect the user to homepage
        return redirect('home_page')

    # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    # category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request=request, template_name='posts_by_category.html', context=context)
