from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Cart(models.Model):
    STATUS = [
        ('open', 'Open'),
        ('closed', 'Closed')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='open')


class CartItem(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)