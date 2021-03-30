from django.urls import path
from . import views

urlpatterns = [
	path('', views.topusers_index, name='topusers_index'),
	path('topic', views.tu_topic.as_view(), name='tu_topic'),
	path('env', views.env_topic.as_view(), name='env_topic'),
	path('health', views.health_topic.as_view(), name='health_topic'),
	path('volume', views.tu_volume.as_view(), name='tu_volume'),
	path('engagement', views.tu_engage, name='tu_engage'),
]