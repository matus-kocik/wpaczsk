from django.views.generic import TemplateView
from media.models import Image
import random

class HomeView(TemplateView):
    template_name = 'main/home.html'