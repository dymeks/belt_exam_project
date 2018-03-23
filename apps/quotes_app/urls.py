from django.conf.urls import url
from . import views  

urlpatterns = [
	url(r'^$', views.index),
	url(r'^users/(?P<user_id>\d+)$',views.show),
	url(r'^quotes$',views.show_quotes),
	url(r'^process$',views.new_quote),
	url(r'^add_favorite/(?P<quote_id>\d+)$',views.add_favorite),
	url(r'^delete_favorite/(?P<quote_id>\d+)$',views.delete_favorite),

]