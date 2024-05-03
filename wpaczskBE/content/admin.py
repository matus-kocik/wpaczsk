from django.contrib import admin
from content.models import Article, Event

admin.site.register([Article, Event])