from django import forms
from .models import Food

class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('name', 'money')
        widgets = {
            'name': forms.TextInput(),
            'money': forms.NumberInput()
        }