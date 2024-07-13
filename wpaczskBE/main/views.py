from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from media.models import Image
from content.models import Article


class HomeView(TemplateView):
    template_name = "main/home.html"
    extra_context = {
        "home_page_card_images": Image.objects.filter(
            card_item=True, template_name="home"
        ),
        "home_page_card_articles": Article.objects.all().order_by("-publication_date")[:3],
        "register_form": UserCreationForm(),
        "login_form": AuthenticationForm(),
    }


class WPAView(TemplateView):
    template_name = "main/wpa.html"


class WPACZSKView(TemplateView):
    template_name = "main/wpa_czsk.html"


class ContactsView(TemplateView):
    template_name = "main/contacts.html"


class LinksView(TemplateView):
    template_name = "main/links.html"


class DonationView(TemplateView):
    template_name = "main/donation.html"
