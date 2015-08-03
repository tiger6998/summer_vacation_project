from django.conf.urls import patterns, url
from movies import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^add_movie/$', views.add_movie, name='add_movie'),
	url(r'^register/$', views.register, name='register'),
	url(r'^detail/(?P<movie_name_slug>[\w\-]+)/$', views.movie, name='movie'),
	url(r'^detail/(?P<movie_name_slug>[\w\-]+)/add_comment/$', views.add_comment, name='add_comment'),
	url(r'^detail/(?P<movie_name_slug>[\w\-]+)/add_picture/$', views.add_picture, name='add_picture'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^about/$', views.about, name='about'),
	url(r'^movie_list/$', views.movielist, name='movie_list'),
	#url(r'^add_people/$', views.add_people, name='add_people'),
	)