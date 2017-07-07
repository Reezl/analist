from django.db import models

class Categorias(models.Model):
	name = models.CharField('Nome', max_length=50)
	slug = models.SlugField('Atalho')
	description = models.TextField('Descrição', blank = True) # Blank  = True / Campo não obrigatório
	
	#start_date = models.DateField('Data de início', null = True, blank = True) # null = True /  Ele pode ser nulo a nível de banco de dados
	
	image = models.ImageField(upload_to = 'categorias/images',verbose_name = 'Imagem', null = True, blank = True)
	
	created_at = models.DateTimeField('Criado em', auto_now_add = True) # Quando foi criado / auto_now_add , coloca a data atual do criamento
	
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)# Atualizado em/ atualiza a data

	
