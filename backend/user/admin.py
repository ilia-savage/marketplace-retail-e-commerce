from django.contrib import admin

from .models import User

from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ContactForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(initial="US"),
        }

@admin.register(User)
class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
