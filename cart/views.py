from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from cart.models import Cart, CartItem
from product.models import Product


@login_required
def cart_view(request):
    cart = get_open_cart(request)
    return render(request, 'cart.html', {'cart': cart})

@login_required()
def get_open_cart(request):
    user = request.user
    open_cart, created = Cart.objects.get_or_create(status='open', user=user)
    return open_cart


@login_required()
def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id', Product.objects.first().id)
        quantity = request.POST.get('quantity', 1)
        cart = get_open_cart(request)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
        cart_item.quantity += int(quantity)
        if cart_item.quantity > 0:
            cart_item.save()
        else:
            cart_item.delete()
    return redirect(request.META.get('HTTP_REFERER', reverse_lazy('cart')))