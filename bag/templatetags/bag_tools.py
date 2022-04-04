""" Import """
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """Calculate directly when user increase the quantity"""
    return price * quantity
