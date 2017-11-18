from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.header_page, name = 'articles'),
    url(r'^articles/all/$', views.articles, name = 'articles'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
]