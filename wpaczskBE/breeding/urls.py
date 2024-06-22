from django.urls import path
from .views import ProjectsView, BreedingView, ListOfMembersView

urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('breeding/', BreedingView.as_view(), name ='breeding'),
    path('list_of_members/', ListOfMembersView.as_view(), name ='list_of_members'),
]