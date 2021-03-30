from django.urls import path
from . import views

urlpatterns = [
	path('', views.cluster_index, name='cluster_index'),
	#path('result', views.jaccard_result.as_view(), name='jaccard_result'),
	path('result', views.jaccard_result.as_view(), name ="jaccard_result"),
]