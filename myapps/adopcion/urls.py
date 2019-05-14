from django.conf.urls import url

from myapps.adopcion.views import index_adopcion

urlpatterns = [
    url(r'^index$', index_adopcion),
]
