from django.urls import path
from . import views

urlpatterns = [
	path('', views.usernetwork_index, name='usernetwork_index'),
	]
