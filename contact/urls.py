from django.urls import path

from contact import views

urlpatterns = [
    path('contact/', views.ContactCreateView.as_view(), name='contact-page'),
    path('contact_confirmation/', views.SentTemplateView.as_view(), name='contact-confirmation'),
]