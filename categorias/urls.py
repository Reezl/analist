# URL CATEGORIAS
from django.conf.urls import patterns, include, url

urlpatterns = patterns('categorias.views',
	url(r'^$', 'categorias', name='index')

) 
	

