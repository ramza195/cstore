import django_filters
from product.models import Product
import generics
from django import forms

from product.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Nume', widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': 'Introduceti numele produsului'}))
    color = django_filters.CharFilter(lookup_expr='icontains', label='Culoare', widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': 'Cautati dupa culoarea dorita'}))
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Pret minim',
                                            widget=forms.NumberInput(attrs={'class': "form-control",
                                                                            'placeholder': 'Introduceti pretul minim al produselor afisate'}))
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Pret maxim',
                                            widget=forms.NumberInput(attrs={'class': "form-control",
                                                                            'placeholder': 'Introduceti pretul maxim al produselor afisate'}))



    class Meta:
        model = Product
        fields = ['name', 'color', 'price_min', 'price_max']


class SearchFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name']