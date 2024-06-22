from django.urls import path
from .views import ImagesView, MoviesView

urlpatterns = [
    path('images/', ImagesView.as_view(), name='images'),
    path('movies/', MoviesView.as_view(), name='movies'),
]
