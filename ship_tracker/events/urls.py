from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.EventCreate.as_view(), name='event-create'),
]
