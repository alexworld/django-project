from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^persons/$', views.user_list, name='user_list'),
    url(r'^(?P<target>\d)$', views.post_list, name='post_list_target'),
    url(r'^(?P<target>\d)/page/(?P<page>\d+)$', views.post_list, name='post_list_next'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^person/(?P<pk>\d+)/$', views.profile, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^post_plus/$', views.post_plus, name='post_plus'),
    url(r'^comment_plus/$', views.comment_plus, name='comment_plus'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url(r'^post/(?P<post>\d+)/create_comment/$', views.create_comment, name='create_comment'),
    url(r'^register/$', views.register, name='register'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^post/(?P<post>\d+)/comment/(?P<pk>\d+)/$', views.edit_comment, name='edit_comment'),
]
