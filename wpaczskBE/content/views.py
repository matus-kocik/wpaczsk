from django.views.generic import TemplateView
from media.models import Image
from content.models import Article


class ArticlesView(TemplateView):
    template_name = "content/articles.html"
    extra_context = {
        "home_page_card_images": Image.objects.filter(
            card_item=True, template_name="home"
        ),
        "home_page_card_articles": Article.objects.all().order_by("-publication_date"),
    }
