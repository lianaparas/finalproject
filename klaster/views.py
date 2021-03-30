from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pandas as pd
import json
from .models import TotalTwCategory, FinalCategory, OriginTwt

  
def cluster_index(request):
    
    og_twt 		= OriginTwt.objects.all()
    paginator 	= Paginator(og_twt, 12) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj 	= paginator.get_page(page_number)

    return render(request, 'cluster_index.html', {'page_obj': page_obj })

class jaccard_result(TemplateView):
	template_name = 'jaccard_result.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["qs"] = TotalTwCategory.objects.all()

#def jaccard_result(request):
#		og_result	= FinalCategory.objects.all()
#		paginator 	= Paginator(og_result, 12) # Show 8 contacts per page.\
##		page_number = request.GET.get('page')
#		page_obj 	= paginator.get_page(page_number)
#
#		return render(request, 'jaccard_result.html', {'page_obj': page_obj})



