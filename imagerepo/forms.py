from django import forms
from .models import ImageView

class ImageViewForm(forms.ModelForm): # form to be used in post_create

    class Meta:
        model = ImageView
        fields = ['title', 'price', 'sold', 'discount', 'cover']