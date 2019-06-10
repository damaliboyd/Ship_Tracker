from django import forms

from .models import Grocery

class GroceryCreateForm(forms.ModelForm):
    item = forms.CharField(
            widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )
    class Meta:
        model = Grocery
        fields = ('item', 'category', 'have',)
