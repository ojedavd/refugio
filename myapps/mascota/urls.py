from django.conf.urls import url

from myapps.mascota.views import index

urlpatterns = [
    url(r'^$', index),
]
