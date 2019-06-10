from django import forms

from .models import Grocery

class PostForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = ('item,', 'category', 'have')


