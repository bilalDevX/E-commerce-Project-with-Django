from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

# def faq(request):
#     return render(request, 'core/faq.html')

# def terms(request):
#     return render(request, 'core/terms.html')

# def privacy(request):
#     return render(request, 'core/privacy.html')

# def refund(request):
#     return render(request, 'core/refund.html')

def contact(request):
    return render(request, 'core/contact.html')
