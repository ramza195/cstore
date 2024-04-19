from django.urls import path

from userextend import views

urlpatterns = [
    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change-password')
]