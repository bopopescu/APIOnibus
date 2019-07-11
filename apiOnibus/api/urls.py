from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^ultimaLocalizacao', UltimaLocalizacao.as_view()),
    url(r'^ultimaLocalizacao/(?P<pk>[0-9]+)$', UltimaLocalizacaoDetalhes.as_view()),
    url(r'^horarioRota', HorarioRota.as_view()),
    url(r'^horarioRota/(?P<pk>[0-9]+)$', HorarioRotaDetalhes.as_view()),
    url(r'^usuario', Usuario.as_view()),
    url(r'^usuario/(?P<pk>[0-9]+)$', UsuarioDetalhes.as_view()),
    url(r'^ultimaLocalizacaoUsuario', UltimaLocalizacaoUsuario.as_view()),
    url(r'^ultimaLocalizacaoUsuario/(?P<pk>[0-9]+)$', UltimaLocalizacaoUsuarioDetalhes.as_view())


    #url(r'^rotas$', RotaList.as_view()),
    #url(r'^rotas/(?P<pk>[0-9]+)$', RotaList.as_view()),
]