from django.core.files.storage import FileSystemStorage

class ContentArticleImageStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'content/static/content'
        super().__init__(*args, **kwargs)

class ContentArticlePDFStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'content/static/content'
        super().__init__(*args, **kwargs)

class ContentEventImageStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'content/static/content'
        super().__init__(*args, **kwargs)

class ContentEventPDFStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'content/static/content'
        super().__init__(*args, **kwargs)
