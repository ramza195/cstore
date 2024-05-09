import django_filters
from django import forms

from product.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Nume', widget=forms.TextInput(attrs={'class':"form-control", 'placeholder': 'Introduceti numele produsului'}))
    # category = django_filters.CharFilter(lookup_expr='icontains', label='Categorie', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Introduceti categoria produsului'}))
    price_max = django_filters.NumberFilter(lookup_expr='lte', label='Pret maxim', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Introduceti pretul maxim al produselor afisate'}))
    price_min = django_filters.NumberFilter(lookup_expr='gte', label='Pret minim', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Introduceti pretul minim al produselor afisate'}))

    class Meta:
        model = Product
        fields = ['name', 'price_max', 'price_min']