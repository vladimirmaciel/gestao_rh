from django.db import models

from apps.funcionarios.models import Funcionario


class Documentos(models.Model):
    descricao = models.CharField(max_length=100, help_text='Descrição do documento')
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT, related_name='documento_funcionario')


    def __str__(self):
        return self.descricao
