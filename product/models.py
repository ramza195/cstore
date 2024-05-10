from django.db import models

from category.models import Category


class Product(models.Model):

    COLOR = [
        ('bleu', 'Bleu'),
        ('roz', 'Roz'),
        ('alb', 'Alb'),
        ('lila', 'Lila'),
        ('verde', 'Verde'),
        ('mov', 'Mov'),
        ('galben', 'Galben')
    ]
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=10, choices=COLOR)
    description = models.TextField()
    image = models.ImageField(upload_to='static/products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name