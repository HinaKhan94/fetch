from .models import Contact
from django.contrib.auth.models import User
from django import forms



class ContactForm(forms.ModelForm):
    """
    It is used on the contact page for any user
    queries
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']