from django.shortcuts import render
from django.http import HttpRequest
from .models import Person, Department
from .models import Product, ProductCategory
from basketapp.models import Basket
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request: HttpRequest):
    title = 'Главная'
    products = Product.objects.all()

    return render(request, 'mainapp/index.html', {
        'title': title,
        'products': products,
    })


def products(request: HttpRequest, id=None):
    title = 'продукты'
    links_categories = ProductCategory.objects.all()
    basket = Basket.objects.filter(user=request.user)

    if id is not None:
        identic_prods = Product.objects.filter(category__pk=id)
    else:
        identic_prods = Product.objects.all()

    return render(request, 'mainapp/products.html', {
        'title': title,
        'links_categories': links_categories,
        'identic_prods': identic_prods,
        'basket': basket
    })


def product_detail(request: HttpRequest, id=None):
    item = get_object_or_404(Product, pk=id)
    identic_prods = Product.objects.exclude(pk=id).filter(category__pk=item.category_id)
    links_categories = ProductCategory.objects.all()



    return render(request, 'mainapp/details.html',{
        'title': f'Товар: {item.name}',
        'item': item,
        'products': identic_prods,
        'links_categories': links_categories,
    })

def contact(request: HttpRequest):
    title = 'Контакты'

    return render(request, 'mainapp/contact.html', {
        'title': title,
    })
