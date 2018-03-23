from django.conf.urls import url
from . import views  

urlpatterns = [
	url(r'^$', views.index),
	url(r'^registration$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^users/(?P<user_id>\d+)$',views.show),
	# url(r'^(?P<user_id>\d+)$',views.show),
	# url(r'^new$', views.new),
	# url(r'^(?P<user_id>\d+)/edit$', views.edit),
	# url(r'^(?P<user_id>\d+)/destroy$', views.delete),
	# url(r'^create$', views.create),
	# url(r'^update$', views.update),
]