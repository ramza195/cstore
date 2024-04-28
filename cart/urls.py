from django.urls import path

from cart import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add-to-cart'),
]