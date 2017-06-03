from __future__ import unicode_literals

from django.db import models
from utils import code_generator, create_shortcode
from django.conf import settings
from validators import validate_url
from django_hosts.resolvers import reverse

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class url_shortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(url_shortURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active = True)
        return qs

    def refresh_shortcodes(self, items = None):
        qs = url_shortURL.objects.filter(id__gte = 1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]

        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i = new_codes)


# Create your models here.
class url_shortURL(models.Model):
    url = models.CharField(max_length = 500, validators = [validate_url])
    shortcode = models.CharField(max_length = SHORTCODE_MAX, unique = True, blank = True)
    count = models.IntegerField(default = 0)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = True)

    objects = url_shortURLManager()

    # Overriding save method of super class models.Model
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = code_generator()
        super(url_shortURL, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.url)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs = {"shortcode": self.shortcode}, host = "www", scheme = "http")
        return url_path
