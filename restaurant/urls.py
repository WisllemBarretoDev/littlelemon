from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/', views.display_menu_item, name='menu_item'),
]
