import collections
import operator

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

from .models import Shoe, Style

def index(request):
    context = {'shoes': Shoe.objects.all()}
    return render(request, 'shoestore/index.html', context)

def shoe(request, shoe_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    style = shoe.styles.order_by('colour', 'size').first()

    return shoe_with_style(request, shoe_id, style.id)

def shoe_with_style(request, shoe_id, style_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    chosen_style = get_object_or_404(Style, pk=style_id)

    if chosen_style.shoe != shoe:
        raise Http404("Chosen style is not for given shoe.")

    context = {'shoe': shoe,
               'chosen_style': chosen_style}

    if chosen_style.image:
        context['image'] = chosen_style.image
    else:
        context['image'] = shoe.image

    return render(request, 'shoestore/shoe_details.html', context)

