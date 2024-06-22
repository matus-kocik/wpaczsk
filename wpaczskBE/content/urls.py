from django.urls import path
from .views import ArticlesView

urlpatterns = [
    path('articles/', ArticlesView.as_view(), name='articles'),
]