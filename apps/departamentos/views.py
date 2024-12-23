from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


# Create your views here.
class DepartamentoListView(LoginRequiredMixin, ListView):
    model = Departamento
    template_name = 'departamentos/departamentos_list.html'
    context_object_name = 'departamentos'

    def get_queryset(self):
        funcionario = self.request.user.funcionario_user
        empresa = funcionario.empresa
        print(f"Funcionario: {funcionario.nome}, Empresa: {empresa.nome}")  # Adicione este print
        return Departamento.objects.filter(empresa=empresa, is_active=True)


class CreateDepartamentoView(LoginRequiredMixin, CreateView):
    model = Departamento
    fields = ['nome', 'empresa', 'is_active']
    template_name = 'departamentos/departamento_form.html'
    success_url = '/departamentos/'

    def get_form(self, form_class=None):
        # Obtém o formulário padrão
        form = super().get_form(form_class)

        # Filtra o campo 'empresa' para mostrar apenas a empresa do usuário logado
        funcionario = self.request.user.funcionario_user
        form.fields['empresa'].queryset = Empresa.objects.filter(id=funcionario.empresa.id)

        return form

    def form_valid(self, form):
        obj_departamento = form.save()
        # funcionario = self.request.user.funcionario_user
        # funcionario.departamentos.add(obj_departamento)
        # funcionario.save()
        return HttpResponse('Departamento criado com sucesso!')  # Exemplo de retorno
