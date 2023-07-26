from io import BytesIO
from PIL import Image
from django.core.files import File


from celery import shared_task



@shared_task
def make_thumbnail(product_id, size=(300, 200)):
    from .models import Product

    product = Product.objects.get(id=product_id)

    img = Image.open(product.image)
    img.convert('RGB')
    img.thumbnail(size)

    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG', quality=85)

    product.thumbnail = File(thumb_io, name=product.image.name)
    product.save()