from django.http import HttpResponse
from django.shortcuts import render


def store(request):
    return HttpResponse("Welcome to the Store Page")