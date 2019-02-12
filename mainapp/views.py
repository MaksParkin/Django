from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from basketapp.models import Basket

import datetime
from .models import ProductCategory, Product


def get_current_basket(current_user):
    if current_user.is_authenticated:
        items = Basket.objects.filter(user=current_user)
    else:
        items = None

    return items


def main(request: HttpRequest):
    title = 'главная'

    products = Product.objects.all()

    return render(request, 'mainapp/index.html', {
        'title': title,
        'products': products,
        'basket': get_current_basket(request.user)
    })


def products(request: HttpRequest, id=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if id is not None:
        identic_products = Product.objects.filter(category__pk=id)
    else:
        identic_products = Product.objects.all()

    return render(request, 'mainapp/products.html', {
        'title': title,
        'links_menu': links_menu,
        'identic_products': identic_products,
        'basket': get_current_basket(request.user)
    })


def product_detail(request: HttpRequest, id=None):
    item = get_object_or_404(Product, pk=id)
    identic_products = Product.objects.exclude(pk=id).filter(category__pk=item.category_id)
    links_menu = ProductCategory.objects.all()

    context = {
        'title': f'Товар: {item.name}',
        'item': item,
        'products': identic_products,
        'links_menu': links_menu,
        'basket': get_current_basket(request.user)
    }

    return render(request, 'mainapp/details.html', context)


def contact(request: HttpRequest):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@chairkshop.ru',
            'address': 'Адрес 1',
        },
        {
            'city': 'Калининград',
            'phone': '+7-777-777-7777',
            'email': 'info_kalinigrad@chairshop.ru',
            'address': 'Адрес 2',
        },
        {
            'city': 'Краснодар',
            'phone': '+7-999-999-9999',
            'email': 'info_krasnodar@chairshop.ru',
            'address': 'Адрес 3',
        },
    ]

    return render(request, 'mainapp/contact.html', {
        'title': title,
        'visit_date': visit_date,
        'locations': locations
    })
