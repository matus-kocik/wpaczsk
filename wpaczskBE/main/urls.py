from django.urls import path
from .views import HomeView, WPAView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('wpa/', WPAView.as_view(), name='wpa'),
]
