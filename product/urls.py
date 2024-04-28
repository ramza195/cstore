from django.urls import path

from product import views

urlpatterns = [
    path('list_products/', views.ProductListView.as_view(), name='list-products'),
    path('get_products/<int:pk>/', views.get_all_products_per_category, name='get-products'),
    path('details_product/<int:pk>/', views.ProductDetailView.as_view(), name='details-product')
]