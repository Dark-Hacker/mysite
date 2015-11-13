from django.shortcuts import render

from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Subject')
    email = forms.EmailField(required=True, **label='Your email address'**)
    message = forms.CharField(widget=forms.Textarea, label='Message')

    def create(self):
        pass
        
