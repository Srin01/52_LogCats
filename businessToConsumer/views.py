from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Item
# Create your views here.

class HomeView(ListView):
    model = Item
    template_name = 'home.html'
