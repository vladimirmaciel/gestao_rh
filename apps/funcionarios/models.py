from django.db import models
from django.contrib.auth.models import User
from pkg_resources import require

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do funcionário')
    user = models.OneToOneField(User, on_delete=models.PROTECT , related_name='funcionario_user')
    departamentos = models.ManyToManyField(Departamento, related_name='funcionario_departamento')
    empresa = models.ForeignKey(Empresa,  on_delete=models.PROTECT, related_name='funcionario_empresa', null=True, blank=True)


    def __str__(self):
        return f'{self.nome}'