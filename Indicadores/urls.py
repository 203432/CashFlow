from django.urls import path, re_path
from django.conf.urls import include

# Importacion de la vista
from Indicadores.views import indicadoresList, indicadoresDetail

urlpatterns = [
    re_path(r'^indicadores/$', indicadoresList.as_view()),
    re_path(r'^indicadores/(?P<pk>\d+)$', indicadoresDetail.as_view())
]