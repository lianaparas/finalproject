from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import SnaReplies

# Create your views here.

def usernetwork_index (request):
	sna_obj = SnaReplies.objects.all()
	paginator = Paginator(sna_obj, 10) # Show 8 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, "usernetwork_index.html", {'page_obj': page_obj})

