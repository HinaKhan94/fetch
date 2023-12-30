from .models import Messages
from django.contrib.auth.models import User
from django import forms



class MessageForm(forms.ModelForm):
    """
    It is used on the contact page for any user
    queries
    """
    class Meta:
        model = Messages
        fields = ['name', 'email', 'message']
