from django.urls import path
from .views import HomeView, WPAView, WPACZSKView, ContactsView, LinksView, DonationView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('wpa/', WPAView.as_view(), name='wpa'),
    path('wpa_czsk/', WPACZSKView.as_view(), name='wpa_czsk'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('links/', LinksView.as_view(), name='links'),
    path('donation/', DonationView.as_view(), name='donation'),
]
