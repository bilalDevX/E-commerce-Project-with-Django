from django.http import HttpResponse
from django.shortcuts import render


# def home(request):
#     return HttpResponse("Welcome to the Home Page")

def home(request):
    return render(request, "core/home.html")
#     return HttpResponse("Welcome to the Home Page")

def about(request):
    return render(request, "core/about.html")
#     return HttpResponse("Welcome to the Home Page")

def contact(request):
    return render(request, "core/contact.html")