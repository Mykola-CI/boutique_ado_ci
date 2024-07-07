from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PZtAHJWHpZp79HegaiKyMJkLC98TpEz9cTcXy78xZ2LUdtto0Npc8q6EYWsIPoNy3gzLLvP86rTVWcND2ZSA5rw00SUwMJZeh',
        'client_secret': 'test bla bla bla',
    }

    return render(request, template, context)
