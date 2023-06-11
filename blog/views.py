from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Product, Category


# Create your views here.
def index(request):
    categories = Category.objects.all().filter(is_active=True)[:8]

    context = {
        'categories': categories,
    }
    return render(request, 'pages/index.html', context)


def catalog(request):
    all_categories = Category.objects.filter(is_active=True)
    paginator = Paginator(all_categories, 12)

    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number)

    # Получение номера текущей страницы
    current_page = categories.number

    # Получение общего количества страниц
    total_pages = categories.paginator.num_pages

    # Определение начальной и конечной страниц для отображения
    start_page = max(current_page - 3, 1)
    end_page = min(current_page + 3, total_pages)

    # Создание списка страниц для отображения
    display_pages = range(start_page, end_page + 1)

    context = {
        'categories': categories,
        'display_pages': display_pages,
    }
    return render(request, 'pages/catalog.html', context)


def category_products(request, category_id):
    category = Category.objects.get(pk=category_id)
    all_products = category.product_set.all()
    paginator = Paginator(all_products, 12)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    # Получение номера текущей страницы
    current_page = products.number

    # Получение общего количества страниц
    total_pages = products.paginator.num_pages

    # Определение начальной и конечной страниц для отображения
    start_page = max(current_page - 3, 1)
    end_page = min(current_page + 3, total_pages)

    # Создание списка страниц для отображения
    display_pages = range(start_page, end_page + 1)
    context = {
        'category': category,
        'products': products,
        'display_pages': display_pages,
    }
    return render(request, 'pages/items.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    similar_products = Product.objects.filter(category=product.category).exclude(pk=product_id)

    if similar_products.count() > 4:
        similar_products = similar_products.order_by('?')[:4]
    else:
        similar_products = similar_products.order_by('?')

    context = {
        'product': product,
        'similar_products': similar_products,
    }
    return render(request, 'pages/item-detail.html', context)


def contacts(request):
    return render(request, 'pages/contacts.html')


def about(request):
    return render(request, 'pages/about.html')