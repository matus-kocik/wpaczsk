from django.contrib import admin
from account.models import Profile, BreederProfile

admin.site.register([Profile, BreederProfile])