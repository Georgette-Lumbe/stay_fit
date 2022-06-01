from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from .models import Contact


class ContactForm(forms.Form):
    """Form for conact page"""

    name = forms.CharField(
                        label='Name',
                        max_length=50,
                        widget=forms.TextInput(attrs={
                                                    'class': 'form-control',
                                                    'placeholder': "Full Name",
                                                    }),
                        )
    subject = forms.CharField(
                        label='Subject',
                        max_length=50,
                        widget=forms.TextInput(attrs={
                                                    'class': 'form-control',
                                                    'placeholder': "Subject",
                                                    }),
                        )
    email = forms.EmailField(
                        label='Email Address',
                        widget=forms.EmailInput(attrs={
                                                'class': 'form-control',
                                                'placeholder': "Email address",
                                                }),
                        )
    message = forms.CharField(
                            label='Message',
                            widget=forms.Textarea(attrs={
                                                'class': 'form-control',
                                                'placeholder': "Message",
                                                }),
                            )

    def save(self):
        data = self.cleaned_data
        contact = Contact(
                    name=data['name'],
                    subject=data['subject'],
                    email=data['email'],
                    message=data['message']
                    )
        contact.save()

    def send_email(self):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("Invalid header, submission failed")
