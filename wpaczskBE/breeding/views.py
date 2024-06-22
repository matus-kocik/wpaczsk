from django.views.generic import TemplateView

class ProjectsView(TemplateView):
    template_name = "breeding/projects.html"
    
class BreedingView(TemplateView):
    template_name = "breeding/breeding.html"