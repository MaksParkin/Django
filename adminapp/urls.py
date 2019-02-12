from django.urls import path
from adminapp.views import users, products, categories

app_name = 'adminapp'

urlpatterns = [
    #CRUD users
    path('users/index', users.index, name='users'),
    path('users/create', users.create, name='user_create'),
    path('users/read/<int:id>', users.read, name='users'),
    path('users/update/<int:id>', users.update, name='user_update'),
    path('users/delete/<int:id>', users.delete, name='user_delete'),
    #CRUD categories
    path('categories/index', categories.index, name='categories'),
    path('categories/create', categories.create, name='categories_create'),
    path('categories/read/<int:id>', categories.read, name='categories_read'),
    path('categories/update/<int:id>', categories.create, name='categories_updatee'),
    path('categories/delete/<int:id>', categories.delete, name='categories_delete'),
    #CRUD products
    path('products/list/<int:category>', products.list_by_category, name='product_category'),
    path('products/create', products.create, name='products_create'),
    path('products/read/<int:id>', products.read, name='products_read'),
    path('products/update/<int:id>', products.create, name='products_update'),
    path('products/delete/<int:id>', products.delete, name='products_delete'),
]