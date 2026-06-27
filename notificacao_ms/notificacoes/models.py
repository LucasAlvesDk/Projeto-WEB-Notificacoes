import secrets
from django.db import models


class Empresa(models.Model):
    """
    Representa um sistema/cliente que usa o microservico.
    Cada empresa recebe um hash unico de 16 caracteres para autenticacao.
    """
    nome = models.CharField(max_length=200, unique=True)
    hash = models.CharField(max_length=16, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.hash:
            self.hash = secrets.token_hex(8)  # 8 bytes = 16 caracteres hex
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome


class Target(models.Model):
    """
    Vincula um usuario de um sistema externo ao microservico.
    O user_id e o ID do usuario no sistema cliente (ex: User.id do portfolio).
    """
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='targets')
    user_id = models.IntegerField()

    class Meta:
        verbose_name = 'Target'
        verbose_name_plural = 'Targets'
        unique_together = ['empresa', 'user_id']  # Nao pode repetir usuario na mesma empresa

    def __str__(self):
        return f'{self.empresa.nome} - User {self.user_id}'


class Notification(models.Model):
    """
    Uma notificacao enviada para um target especifico.
    """
    target = models.ForeignKey(Target, on_delete=models.CASCADE, related_name='notificacoes')
    mensagem = models.TextField()
    is_read = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Notificacao'
        verbose_name_plural = 'Notificacoes'
        ordering = ['-criado_em']

    def __str__(self):
        status = 'Lida' if self.is_read else 'Nao lida'
        return f'[{status}] {self.mensagem[:50]}'
