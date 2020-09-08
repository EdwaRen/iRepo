from django.contrib import admin

from .models import Post
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'sold', 'discount', 'image_tag', 'display_price')


admin.site.register(Post, PostAdmin)
