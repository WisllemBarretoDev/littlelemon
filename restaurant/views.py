from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def home(request):
    return HttpResponse('Home')

def menu(request):
    menu_data = models.Menu.objects.all()
    return render('request', 'restaurant/menu.html', {'menu' : menu_data} )


