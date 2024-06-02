from django.views.generic import TemplateView
from media.models import Image
import random

class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = list(Image.objects.filter(carousel=True))
        random.shuffle(images)
        context['carousel_images'] = images
        return context
