from django.shortcuts import render
from django.http import HttpRequest
from .models import Person, Department
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
        'products': products,
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

    identic_prods = [
        {
            'name': 'Отличный стул',
            'desc': 'Не оторваться.',
            'image_src': 'product-11.jpg',
            'alt': 'продукт 11'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Комфортно.',
            'image_src': 'product-21.jpg',
            'alt': 'продукт 21'
        },
        {
            'name': 'Стул премиального качества',
            'desc': 'Просто попробуйте.',
            'image_src': 'product-31.jpg',
            'alt': 'продукт 31'
        },
    ]

    return render(request, 'mainapp/products.html', {
        'title': title,
        'links_categories': links_categories,
        'identic_prods': identic_prods
    })

def contact(request: HttpRequest):
    title = 'Контакты'

    return render(request, 'mainapp/contact.html', {
        'title': title,
    })

def company_index(request: HttpRequest):
    dept = Department.objects.all()
    pass

def company_view(request: HttpRequest, id=None):
    dept = Department.objects.get(id=id)
    pass