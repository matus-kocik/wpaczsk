from django.urls import path
from .views import ListOfSpeciesView

urlpatterns = [
    path('list_of_species/', ListOfSpeciesView.as_view(), name='list_of_species'),
]
