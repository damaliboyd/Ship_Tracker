from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from events.models import Event
from django.http import HttpResponse
from django.urls import reverse_lazy

class EventCreate(CreateView):
    model = Event
    fields = ["event_title, event_date,event_des"]

"""
class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('event_list')

class EventList(ListView):
    title = "Event List View"

    def get (self, request):
        return HttpResponse(self.title)

class EventDetail(DetailView):
    title = "Event Detail View"

    def get (self, request):
        return HttpResponse(self.title)
"""
