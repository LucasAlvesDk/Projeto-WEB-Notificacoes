from django.contrib import admin
from .models import Empresa, Target, Notification


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'hash']
    readonly_fields = ['hash']


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ['empresa', 'user_id']
    list_filter = ['empresa']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['target', 'mensagem_curta', 'is_read', 'criado_em']
    list_filter = ['is_read', 'target__empresa']
    list_editable = ['is_read']

    def mensagem_curta(self, obj):
        return obj.mensagem[:60] + '...' if len(obj.mensagem) > 60 else obj.mensagem
    mensagem_curta.short_description = 'Mensagem'
