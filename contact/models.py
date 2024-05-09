from django.db import models

class Contact(models.Model):
    nume = models.CharField(max_length=255)
    subiect = models.CharField(max_length=255)
    mesaj = models.TextField()
    email = models.EmailField()
    numar_telefon = models.CharField(max_length=11)

    def __str__(self):
        return self.subiect
