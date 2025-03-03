from django.urls import path
from .views import home, about, contact
# ,faq, terms, privacy, refund

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    # path('faq/', faq, name='faq'),
    # path('terms-and-conditions/', terms, name='terms'),
    # path('privacy-policy/', privacy, name='privacy'),
    # path('refund-policy/', refund, name='refund'),
]
