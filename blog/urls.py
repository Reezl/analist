from django.conf.urls import patterns,include, url
from . import views
from  django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
'''
urlpatterns = [
	url(r'^$', views.base, name='base'),
	##
	url(r'^categorias/', include('categorias.urls', namespace = 'categorias')),
	##
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/$', views.post_list, name='post_list'), # HOME
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^contato/$',views.contact,name='contact'),
	
]
'''
urlpatterns = patterns('',
	url(r'^$', views.base, name='base'),
	##
	url(r'^categorias/', include('categorias.urls', namespace = 'categorias')),
	##
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/$', views.post_list, name='post_list'), # HOME
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^contato/$',views.contact,name='contact'),

)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
