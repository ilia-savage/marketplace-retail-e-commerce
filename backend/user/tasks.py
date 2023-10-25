import requests

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from celery import shared_task

from product.models import Product


@shared_task
def send_email(subject, message, to_email="test@test.test"):    
    send_mail(subject, message, "Iltech@gmail.com", [to_email]) 

@shared_task
def send_promo():
    promo_product = Product.objects.order_by('?')[0]
    html_message = render_to_string('email.html', {'product': promo_product})
    
    send_mail("Iltech - новые товары", "haha", "Iltech@gmail.com", ['test@test.test'], html_message=html_message)