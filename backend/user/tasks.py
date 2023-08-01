from django.core.mail import send_mail

from celery import shared_task


@shared_task
def send_email(subject, message):

    send_mail(
        subject,
        message,
        'settings.EMAIL_HOST_USER',
        ['test-uurfrsn7o@srv1.mail-tester.com'],
        fail_silently=False
    )       