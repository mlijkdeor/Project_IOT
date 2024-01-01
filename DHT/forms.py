from django import forms

from .models import Dht11

class NewDht11(forms.ModelForm):
    class Meta:
        model = Dht11
        fields = ('temp' , 'hum')

    temp = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Your temperature',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    hum = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Your humidity',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

