from django.shortcuts import render
from .models import Categorias

def categorias(request):
	template_name = 'categorias/categorias.html'
	categorias = Categorias.objects.all()
	context = {
		'categorias': categorias
		
	}
	
	return render(request, template_name, context)
