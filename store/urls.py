from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("<slug:slug>/", views.product_details, name="product_details"),
]
