from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Shoe

def index(request):
    context = {'shoes': Shoe.objects.all()}
    return render(request, 'shoestore/index.html', context)

def shoe(request, shoe_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    return HttpResponse("Shoe: {}".format(shoe.name))

