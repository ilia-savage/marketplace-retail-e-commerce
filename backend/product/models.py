from io import BytesIO
from PIL import Image
from django.core.files import File


from django.db import models
from django.urls import reverse
# Create your models here.
from category.models import Category
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Name", max_length=255)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024)
    specs = models.JSONField(null=True, blank=True)
    discount = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name="Product"
        verbose_name_plural="Products"

    def __str__(self):
        return self.name
    
    def make_thumbnail(self, image, size=(300, 200)):
        print(image)
        img = Image.open(image)
        img.convert('RGBA')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        
        if self.image:
            
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        return ''