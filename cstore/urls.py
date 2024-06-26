"""
URL configuration for cstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views, views

from userextend.forms import AuthenticationNewForm, ChangePasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),
    path('change-password/', views.PasswordChangeView.as_view(form_class=ChangePasswordForm), name='password-change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password-change-done'),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('', include('django.contrib.auth.urls')),
    path('', include('userextend.urls')),
    path('', include('category.urls')),
    path('', include('product.urls')),
    path('', include('cart.urls')),
    path('', include('contacts.urls'))
]
