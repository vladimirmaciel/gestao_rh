from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import Empresa
from ..funcionarios.models import Funcionario


class EmpresaCreateView(LoginRequiredMixin,CreateView):
    model = Empresa
    fields = ['nome']  # Exemplo de campos
    template_name = 'empresas/empresa_form.html'
    success_url = '/empresas/'  # Redirecionar após criação

    def form_valid(self, form):
        obj_empresa = form.save()
        funcionario = self.request.user.funcionario_user
        funcionario.empresa = obj_empresa
        funcionario.save()
        return HttpResponse('Empresa criada com sucesso!')  # Exemplo de retorno
