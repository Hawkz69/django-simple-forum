from django.db import models

class Curse(models.Model):
    name = models.CharField('Nome', max_length=150)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data inicio', blank=True, null=True)
    image = models.ImageField('Imagem', upload_to='curses/image')
    created_at = models.DateTimeField('Criaçao', auto_now_add=True)
    updated_at = models.DateTimeField('Alteracao', auto_now=True)
    
    
    
