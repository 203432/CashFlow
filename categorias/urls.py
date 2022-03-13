from django.urls import path, re_path
from django.conf.urls import include


# Importacion de la vista
from categorias.views import CategoriaList, CategoriaDetail

urlpatterns = [
    re_path(r'^categoria/$', CategoriaList.as_view()),
    re_path(r'^categoria/(?P<pk>\d+)$', CategoriaDetail.as_view()),
]
