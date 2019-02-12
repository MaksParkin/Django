from django.db import models

# Create your models here.
from mainapp.models import ProductCategory
from django.forms import ModelForm


class CategoryEditForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'