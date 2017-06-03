from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomeView, RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', RedirectView.as_view(), name = 'scode'),
]
