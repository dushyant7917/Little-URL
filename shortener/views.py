from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from models import url_shortURL
from forms import SubmitUrlForm

# Create your views here.
class HomeView(View):
	def get(self, request, *args, **kwargs):
		form = SubmitUrlForm()
		context = {
			"title": "Little URL",
			"form": form
		}
		return render(request, "shortener/home.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			"title": "Submit URL",
			"form": form
		}
		template = "shortener/home.html"

		if form.is_valid():
			new_url = form.cleaned_data.get('url')
			obj, created = url_shortURL.objects.get_or_create(url = new_url)
			context = {
				"object": obj,
				"created": created
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"

		return render(request, template, context)

class RedirectView(View):
	def get(self, request, shortcode = None, *args, **kwargs):
		qs = url_shortURL.objects.get(shortcode__iexact = shortcode)
		qs.count += 1
		qs.save()

		return HttpResponseRedirect(qs.url)
