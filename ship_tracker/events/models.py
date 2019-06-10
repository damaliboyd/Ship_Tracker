from django.db import models

class Event (models.Model):
    event_title = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    event_des =  models.TextField()
