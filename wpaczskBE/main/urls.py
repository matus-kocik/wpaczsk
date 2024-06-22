from django.urls import path
from .views import HomeView, WPAView, WPACZSKView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('wpa/', WPAView.as_view(), name='wpa'),
    path('wpa_czsk/', WPACZSKView.as_view(), name='wpa_czsk'),
]
