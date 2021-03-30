from django.urls import path
from . import views

urlpatterns = [
	#path('', views.locations_index, name='locations_index'),
	path('', views.locs_index.as_view(), name='locations_index'), #You need use as_view() at the end of class based views when declaring in the urls:
	path('map', views.locs_map, name='locs_map'),
	]
