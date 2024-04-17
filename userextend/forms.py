from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Introduceti adresa de email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Introduceti parola asociata contului'})


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Introduceti prenumele'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Introduceti numele'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Introduceti adresa de email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Introduceti o parola'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pentru verificare, mai introduceti o data parola'})