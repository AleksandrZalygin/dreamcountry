from .models import Country
from django.forms import ModelForm, TextInput, Select

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['climate', 'world', 'work', 'medicine', 'citizenship',]

        widgets = {
            'climate': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Какой климат предпочитаете?',
            }),
            'world': Select(attrs={ 
                'class': 'form-control',
                'placeholder': 'В какой части света хотите жить?'
            }),
            'work': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Работать будете всё равно в России?'
            }),
            'medicine': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Важна ли вам бесплатная или дешёвая медицина?'
            }),
            'citizenship': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Важно ли быстро получить гражданство другой страны?'
            }),
        }