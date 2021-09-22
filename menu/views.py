from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza


# Create your views here.
def index(request):
    pizzas = Pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html', {'pizzas': pizzas})


def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('price')
    json = serializers.serialize('json', pizzas)
    return HttpResponse(json)
