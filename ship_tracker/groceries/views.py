from .models import Grocery
from .forms import GroceryCreateForm
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

class GroceryCreateView(CreateView):
    model = Grocery
    fields = ['item', 'category', 'have']


class GroceryDetailView(DetailView):
    model = Grocery


class GroceryListView(ListView):
    model = Grocery

class GroceryTemplateView(TemplateView):
    template_name= "base.html"  