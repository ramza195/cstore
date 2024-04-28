from django.urls import path

from category import views

urlpatterns = [
    path('list_categories/', views.CategoryListView.as_view(), name='list-categories')
]

