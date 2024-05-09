from django import forms

from contacts.models import Contacts


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nume'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Introduceti numele'})
        self.fields['subiect'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Scrieti subiectul mesajului'})
        self.fields['mesaj'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrieti situatia intampinata'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Introduceti adresa de email'})
        self.fields['numar_telefon'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Introduceti un telefon de contact'})