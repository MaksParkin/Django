from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def index(request: HttpRequest):
    title = 'Главная'

    products = [
        {
            'name': 'Отличный стул',
            'desc': 'Расположитесь комфортно.',
            'img_src': 'product-1.jpg',
            'img_href': '/product/1/',
            'alt': 'product 1'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'img_src': 'product-2.jpg',
            'img_href': '/product/2/',
            'alt': 'product 2'
        },
    ]

    return render(request, 'mainapp/index.html', {
        'title': title,
        'products': products
    })

def products(request: HttpRequest):
    title = 'Продукты'

    links_categories = [
        {'href': '/products/0/', 'name': 'все'},
        {'href': '/products/1/', 'name': 'дом'},
        {'href': '/products/2/', 'name': 'офис'},
        {'href': '/products/3/', 'name': 'модерн'},
        {'href': '/products/4/', 'name': 'классика'},
    ]

    return render(request, 'mainapp/products.html', {
        'title': title,
        'links_categories': links_categories,
    })

def contact(request: HttpRequest):
    title = 'Контакты'

    return render(request, 'mainapp/contact.html', {
        'title': title,
    })
