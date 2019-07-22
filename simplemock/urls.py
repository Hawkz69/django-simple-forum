from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .core.views import home, contact
# from .curse.urls import curses

urlpatterns = [
    path('', home, name='home'),
    path('cursos/', include(('simplemock.curse.urls', 'curse'), namespace='curses')),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
]
