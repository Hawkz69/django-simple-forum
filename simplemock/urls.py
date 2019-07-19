from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from simplemock.core.views import home, contact

urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('admin/', admin.site.urls),
]
