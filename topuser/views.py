from django.shortcuts import render
from django.views.generic import TemplateView
#import django_tables2
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.views.generic import ListView
from .models import TopTwsScore, TopUserVolume, TopUserEco, TopUserEnv, TopUserHealth

# Create your views here.

def topusers_index(request):
	return render(request, 'topusers_index.html', {})

class tu_topic(TemplateView):
	template_name = 'topic_eco.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["qs"] = TopUserEco.objects.all()
		return context

class env_topic(TemplateView):
	template_name = 'topic_env.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["qs"] = TopUserEnv.objects.all()
		return context

class health_topic(TemplateView):
	template_name = 'topic_health.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["qs"] = TopUserHealth.objects.all()
		return context

#def tu_volume(request):
#	return render(request, "volume.html", {})

class tu_volume(TemplateView):
	template_name = 'volume.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["qs"] = TopUserVolume.objects.all()
		return context


def tu_engage(request):
	engage_obj = TopTwsScore.objects.all()
	paginator = Paginator(engage_obj, 8) # Show 8 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, "engage.html", {'page_obj': page_obj })

