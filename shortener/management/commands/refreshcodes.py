from django.core.management.base import BaseCommand, CommandError

from shortener.models import url_shortURL

class Command(BaseCommand):
    help = "Refreshes the short codes for every url"

    def add_arguments(self, parser):
        parser.add_argument('--items', type = int)

    def handle(self, *args, **options):
        print(options)
        return url_shortURL.objects.refresh_shortcodes(items = options['items'])
