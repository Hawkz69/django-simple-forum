from django.db import models

class Curse(models.Model):
    name = models.CharField('Nome', max_length=150)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data inicio', blank=True, null=True)
    image = models.ImageField('Imagem', upload_to='curses/image', blank=True, null=True)
    created_at = models.DateTimeField('Criaçao', auto_now_add=True)
    updated_at = models.DateTimeField('Alteracao', auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ["name"]
    
    
    
