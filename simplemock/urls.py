from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from simplemock.core.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]
