from django.shortcuts import render
from django.http import HttpResponse
from .models import Curse

def index(request):
    curses = Curse.objects.all()
    context = {'courses': curses}
    print(context)
    return render(request, 'curses/index.html', context)