from django.views.generic import TemplateView


class ImagesView(TemplateView):
    template_name = "media/images.html"
    
class MoviesView(TemplateView):
    template_name = "media/movies.html"