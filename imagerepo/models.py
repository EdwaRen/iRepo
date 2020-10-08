from django.db import models
from django.utils.html import mark_safe
from decimal import Decimal


class ImageView(models.Model):
    price = models.DecimalField(decimal_places = 2, max_digits=6)
    title = models.TextField(default="")
    sold = models.BooleanField(default=False)
    discount = models.DecimalField(decimal_places = 2, max_digits=4)
    cover = models.ImageField(upload_to='images/')

    def image_tag(self):
        if self.cover:
            print('<img src="media/%s" style="width: 45px; height:45px;" />' % self.cover)
            return mark_safe('<img src="http://localhost:8000/media/%s" style="width: 45px; height:45px;" />' % self.cover)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def display_price(self):
        return '%.2f' % (self.price - self.price*self.discount*Decimal(0.01))

    def __str__(self):
        return self.title + ", Price: " + str(self.price) + ", Sold: " + str(self.sold) + ", Discount: " + str(self.discount)