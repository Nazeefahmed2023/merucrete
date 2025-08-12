# forms.py

from django import forms
from .models import CarouselSlide

class CarouselSlideForm(forms.ModelForm):
    class Meta:
        model = CarouselSlide
        fields = ['title', 'description', 'background_color', 'image1', 'image2', 'image3']
    
    # Optional: Making fields required
    title = forms.CharField(max_length=255, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    background_color = forms.CharField(max_length=7, required=True)
    image1 = forms.ImageField(required=True)
    image2 = forms.ImageField(required=True)
    image3 = forms.ImageField(required=True)
