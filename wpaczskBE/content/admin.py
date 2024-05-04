from django.contrib import admin
from content.models import Article, Event, Comment

admin.site.register([Article, Event, Comment])