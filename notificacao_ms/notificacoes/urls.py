from django.urls import path
from . import views

urlpatterns = [
    path(
        'api/notificacoes/nao-lidas/',
        views.NotificacoesNaoLidasCountView.as_view(),
        name='notificacoes-nao-lidas',
    ),
    path(
        'api/notificacoes/',
        views.NotificacoesListView.as_view(),
        name='notificacoes-list',
    ),
    path(
        'api/notificacoes/criar/',
        views.NotificacaoCreateView.as_view(),
        name='notificacao-criar',
    ),
    path(
        'api/notificacoes/<int:pk>/lida/',
        views.NotificacaoMarcarLidaView.as_view(),
        name='notificacao-marcar-lida',
    ),
]