""" Import """
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ Check the bag  """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': pk_test_51KlIeaHHswvPKjGPUrPO2dBUKv7gKi0IraN5X1hK8qJLdmGUDWktvibLrweYCGf8CgSt7ZAwfUJsKkxZVmejv5uy00GrNqTqXy,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
