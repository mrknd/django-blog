from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q

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


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': single_blog,
    }
    return render(request=request, template_name='blogs.html', context=context)


def search(request):
    keyword = request.GET.get('keyword')

    blogs = Blog.objects.filter(
        Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),
        status='Published')

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    print(blogs)
    return render(request=request, template_name='search.html', context=context)
