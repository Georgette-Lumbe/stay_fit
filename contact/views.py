from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import ContactForm


# Contact Form view

class ContactFormView(FormView):
    """View for contact page"""

    template_name = 'contact/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        form.save()
        form.send_email()
        messages.success(self.request, 'Message submitted successfully')
        return super().form_valid(form)


# Contact Success view

class ContactSuccessView(TemplateView):
    """Page to display on successful submission of contact"""
    template_name = 'contact/contact_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "Your message is successfully submitted."
        return context
