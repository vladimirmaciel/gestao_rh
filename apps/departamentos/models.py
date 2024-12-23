from django.db import models

from apps.empresas.models import Empresa


class Departamento(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do departamento')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, related_name='departamento_empresa')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
