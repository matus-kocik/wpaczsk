from django.urls import path
from .views import ListOfMembersView, LoginView, RegisterView, CustomLogoutView

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("logout", CustomLogoutView.as_view(), name="logout"),
    path('list_of_members/', ListOfMembersView.as_view(), name ='list_of_members'),
]