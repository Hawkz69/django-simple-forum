# Generated by Django 2.2.3 on 2019-07-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data inicio')),
                ('image', models.ImageField(upload_to='curses/image', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criaçao')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Alteracao')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['name'],
            },
        ),
    ]
