from django.urls import path
from .views import ListOfMembersView

urlpatterns = [
    path('list_of_members/', ListOfMembersView.as_view(), name ='list_of_members'),
]