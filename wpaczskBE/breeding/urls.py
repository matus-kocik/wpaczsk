from django.urls import path
from .views import ProjectsView, BreedingView

urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('breeding/', BreedingView.as_view(), name ='breeding'),
]