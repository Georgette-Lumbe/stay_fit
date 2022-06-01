from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


class DeliveryView(TemplateView):
    """View to display delivery info page"""
    template_name = 'home/delivery.html'
