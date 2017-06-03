from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'little-url-7917', settings.ROOT_URLCONF, name = 'little-url-7917'),
    host(r'(?!little-url-7917).*', 'url_short.hostsconf.urls', name = 'wildcard'),
)
