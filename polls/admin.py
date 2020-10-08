from django.contrib import admin

from .models import ImageView
from django.utils.html import format_html

class ImageViewAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'sold', 'discount', 'image_tag', 'display_price')


admin.site.register(ImageView, ImageViewAdmin)
