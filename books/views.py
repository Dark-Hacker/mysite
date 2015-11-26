from django.shortcuts import render
from django.http import HttpResponse
from django import forms

from books.models import Book


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Subject')
    email = forms.EmailField(required=True, label='Your email address')
    message = forms.CharField(widget=forms.Textarea, label='Message')

    def create(self):
        pass

        
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'error': error})
