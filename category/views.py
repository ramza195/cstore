from django.shortcuts import render
from django.views.generic import ListView

from category.models import Category


class CategoryListView(ListView):
    template_name = 'category/list_of_categories.html'
    model = Category
    context_object_name = 'all_categories'
