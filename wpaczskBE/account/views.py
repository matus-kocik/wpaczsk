from django.views.generic import TemplateView
    
class ListOfMembersView(TemplateView):
    template_name = "account/list_of_members.html"