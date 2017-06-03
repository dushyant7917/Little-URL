from django.contrib import admin

# Register your models here.
from .models import url_shortURL

admin.site.register(url_shortURL)
