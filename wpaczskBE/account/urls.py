from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import ListOfMembersView, LoginView, RegisterView

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("logout", LogoutView.as_view(next_page='home'), name="logout"),
    path('list_of_members/', ListOfMembersView.as_view(), name ='list_of_members'),
]