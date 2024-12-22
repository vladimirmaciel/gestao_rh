from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from apps.departamentos.models import Departamento


# Create your views here.
class DepartamentoListView(LoginRequiredMixin, ListView):
    model = Departamento
    template_name = 'departamentos/departamentos_list.html'
    context_object_name = 'departamentos'

    def get_queryset(self):
        funcionario = self.request.user.funcionario_user
        return Departamento.objects.filter(funcionario_departamento=funcionario)