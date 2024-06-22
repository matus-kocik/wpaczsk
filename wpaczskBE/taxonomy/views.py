from django.views.generic import TemplateView

class ListOfSpeciesView (TemplateView):
    template_name = "taxonomy/list_of_species.html"