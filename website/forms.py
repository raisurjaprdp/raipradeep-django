# website/forms.py

from django import forms
from hcaptcha.fields import hCaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your Name', 'required': True
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Your Email', 'required': True
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5, 'required': True
    }))
    hcaptcha = hCaptchaField() # Correct indentation
