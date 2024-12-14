from django.contrib import admin
from .models import Empresa
from ..departamentos.models import Departamento
from ..funcionarios.models import Funcionario

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Funcionario)
admin.site.register(Departamento)

