from django.views.generic import TemplateView
from media.models import Image

class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images= list(Image.objects.filter(card_item = True, template_name = "home"))
        context["card_images"] = images
        return context
    
class WPAView(TemplateView):
    template_name = "main/wpa.html"
    
class WPACZSKView(TemplateView):
    template_name = "main/wpa_czsk.html"
