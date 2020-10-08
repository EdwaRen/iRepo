from django import forms
from .models import ImageView

class ImageViewForm(forms.ModelForm):

    class Meta:
        model = ImageView
        fields = ['title', 'price', 'sold', 'discount', 'cover']