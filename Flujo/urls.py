from django.urls import path, re_path
from django.conf.urls import include

# Importacion de la vista
from Flujo.views import FlujoEfecList, FlujoEfecDetail

urlpatterns = [
    re_path(r'^flujo/$', FlujoEfecList.as_view()),
    re_path(r'^flujo/(?P<pk>\d+)$', FlujoEfecDetail.as_view()),
]