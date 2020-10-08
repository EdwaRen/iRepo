from django.db import models
from django.utils.html import mark_safe
from decimal import Decimal


class ImageView(models.Model):
    # The original total price for the item
    price = models.DecimalField(decimal_places = 2, max_digits=6)
    
    # Title of the item
    title = models.TextField(default="")

    # Mark whether or not this item has been sold yet
    sold = models.BooleanField(default=False)

    # Percent discount for the item
    discount = models.DecimalField(decimal_places = 2, max_digits=5)
    
    # The actual image
    cover = models.ImageField(upload_to='images/')

    def image_tag(self): # Display the image as a thumbnail in the Django admin
        if self.cover:
            print('<img src="media/%s" style="width: 45px; height:45px;" />' % self.cover)
            return mark_safe('<img src="http://localhost:8000/media/%s" style="width: 45px; height:45px;" />' % self.cover)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def display_price(self): # Show the item's price after applying the discount
        return '%.2f' % (self.price - self.price*self.discount*Decimal(0.01))

    def __str__(self): # A summary of the item in Django admin
        return self.title + ", Price: " + str(self.price) + ", Sold: " + str(self.sold) + ", Discount: " + str(self.discount)