from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from contacts.forms import ContactForm
from contacts.models import Contacts
from cstore.settings import EMAIL_HOST_USER


class ContactCreateView(CreateView):
    template_name = 'contact/contact.html'
    model = Contacts
    form_class = ContactForm
    success_url = reverse_lazy('contact-confirmation')

    def form_valid(self, form):
        new_contact = form.save(commit=False)
        new_contact.nume = new_contact.nume.title()
        new_contact.save()
        details_contact = {
            'new_contact': new_contact
        }
        subiect = 'C-Store Contact - ' + new_contact.subiect
        html_message = get_template('contact/mail.html').render(details_contact)
        send_mail(
            subject=subiect,
            message='',
            html_message=html_message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[new_contact.email, EMAIL_HOST_USER],
        )
        return redirect('contact-confirmation')

class SentTemplateView(TemplateView):
    template_name = 'contact/contact_confirmation.html'