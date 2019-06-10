from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('grocery/create/', views.GroceryCreateView.as_view(), name='grocery_create'),
    path('grocery/detail/<int:pk>', views.GroceryDetailView.as_view(), name='groceries-detail'),
    path('grocery/template', views.GroceryTemplateView.as_view(), name='base'),
    path('grocery/list', views.GroceryListView.as_view(), name='grocery_list'),
]
