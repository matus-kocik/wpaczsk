from media.models import Image

def carousel_images(request):
    images = Image.objects.filter(carousel=True)
    return {'carousel_images': images}
