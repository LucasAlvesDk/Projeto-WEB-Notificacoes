from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'mensagem', 'is_read', 'criado_em']
        read_only_fields = ['id', 'criado_em']


class NotificationCreateSerializer(serializers.Serializer):
    """
    Serializer para criar notificacoes via API.
    Recebe user_id e mensagem. O target e resolvido automaticamente
    a partir do X-Api-Key (empresa) + user_id do body.
    """
    user_id = serializers.IntegerField()
    mensagem = serializers.CharField()
