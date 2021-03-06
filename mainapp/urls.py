from django.urls import path

import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    path('index/', controller.products, name='index'),
    path('page/<int:page>', controller.products, name='page'),
    path('<int:id>/', controller.products, name='category'),
    path('details/<int:id>/', controller.product_detail, name='details'),
]
