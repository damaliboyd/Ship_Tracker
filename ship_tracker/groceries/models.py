from django.db import models
from django.urls import reverse
# Create your models here.


class Grocery(models.Model):
    item = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    have = models.BooleanField()

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('groceries-detail', kwargs={'pk':self.pk})