""" Import """
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = None
    shoesize = None
    if "product_size" or "product_shoesize" in request.POST:
        if "product_size" in request.POST:
            size = request.POST.get("product_size", False)
        else:
            shoesize = request.POST.get("product_shoesize", False)

    bag = request.session.get("bag", {})

    if size or shoesize:
        if size:
            if item_id in list(bag.keys()):
                if size in bag[item_id]["items_by_size"].keys():
                    bag[item_id]["items_by_size"][size] += quantity
                    messages.success(
                        request,
                        f'Updated size {size.upper()} {product.name} quantity \
                            to {bag[item_id]["items_by_size"][size]}',
                    )
                else:
                    bag[item_id]["items_by_size"][size] = quantity
                    messages.success(
                        request, f"Added size {size.upper()} \
                            {product.name} to your bag")
            else:
                bag[item_id] = {"items_by_size": {size: quantity}}
                messages.success(
                    request, f"Added size \
                        {size.upper()} {product.name} to your bag")
        else:
            if item_id in list(bag.keys()):
                if shoesize in bag[item_id]["items_by_shoesize"].keys():
                    bag[item_id]["items_by_shoesize"][shoesize] += quantity
                    messages.success(
                        request,
                        f'Updated shoesize {shoesize.capitalize()} {product.name} \
                            quantity to \
                                {bag[item_id]["items_by_shoesize"][shoesize]}',
                    )
                else:
                    bag[item_id]["items_by_shoesize"][shoesize] = quantity
                    messages.success(request, f"Added \
                        {shoesize.capitalize()} {product.name} to your bag")
            else:
                bag[item_id] = {"items_by_shoesize": {shoesize: quantity}}
                messages.success(request, f"Added \
                    {shoesize.capitalize()} {product.name} to your bag")
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f"Updated {product.name} \
                quantity to {bag[item_id]}")
        else:
            bag[item_id] = quantity
            messages.success(request, f"Added {product.name} to your bag")

    request.session["bag"] = bag
    return redirect(redirect_url)
