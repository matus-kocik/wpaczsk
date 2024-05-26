from media.models import Image

def carousel_images(request):
    """
    EN: Fetches images that are marked for display in the carousel.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            dict: A dictionary containing the queryset of images marked for the carousel under the key 'carousel_images'.

    SK: Načíta obrázky, ktoré sú označené na zobrazenie v karuseli.
        Argumenty:
            request (HttpRequest): Objekt HTTP požiadavky.
        Návratová hodnota:
            dict: Slovník obsahujúci queryset obrázkov označených pre karusel pod kľúčom 'carousel_images'.
    """
    images = Image.objects.filter(carousel=True)
    return {'carousel_images': images}
