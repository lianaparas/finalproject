from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage_view, name='homepage'),
	path('info', views.info_view, name='info'),
	path('menu', views.info_view, name='menu'),
	path('topuser', views.info_view, name='topuser'),
]