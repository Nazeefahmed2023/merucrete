from django import forms
from .models import Slide

class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['title', 'subtitle', 'background_image', 'shape1', 'shape2', 'shape3', 'shape_class']
