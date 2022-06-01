from django.shortcuts import render
from django.views.generic.base import TemplateView


# Home view

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


# Delivery view

class DeliveryView(TemplateView):
    """View to display delivery info page"""
    template_name = 'home/delivery.html'


# Faqs view

class FaqsView(TemplateView):
    """View to display FAQs page"""
    template_name = 'home/faqs.html'
