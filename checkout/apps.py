""" Import """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Checkout Config class """
    name = 'checkout'

    def ready(self):
        import checkout.signals
