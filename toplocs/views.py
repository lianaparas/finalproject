from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Locsdata

# Create your views here.
class locs_index(TemplateView):
	template_name = 'locs_index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["qs"] = Locsdata.objects.all()
		return context



#def locations_index (request):
#	return render(request, "locs_index.html", {})

def locs_map (request):
	return render(request, "top_locations_map.html", {})