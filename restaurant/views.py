from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def home(request):
    return HttpResponse('Home')

def menu(request):
    menu_data = models.Menu.objects.all()
    return render('request', 'restaurant/menu.html', {'menu' : menu_data} )

def display_menu_item(request, pk=None):
    if pk:
        menu_item = models.Menu.objects.get(pk=pk)
    else:
        menu_item = ''

    return render(request, 'restaurant/menu_item.html', {'menu_item' : menu_item})


