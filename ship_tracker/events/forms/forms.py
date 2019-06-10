from django.forms import ModelForm
from event.models import Events

class EventForm(ModelForm):
    class Meta:
        model = event
        fields = ['event_title', 'event_date', 'event_des']
