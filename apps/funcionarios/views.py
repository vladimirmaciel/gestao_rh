from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from apps.funcionarios.models import Funcionario


def home(request):
    return HttpResponse('Olá mundo!')


class FuncionarioCreate(LoginRequiredMixin, CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    template_name = 'funcionarios/funcionario_form.html'
    success_url = reverse_lazy('funcionarios:list')

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario_user.empresa
        funcionario.user = self.create_user_for_funcionario(funcionario)
        funcionario.save()
        return super().form_valid(form)


    def create_user_for_funcionario(self, funcionario):
      nome_parts = funcionario.nome.split()
      username = ''.join(nome_parts[:2])
      return User.objects.create_user(username=username)


class ListFuncionariosView(LoginRequiredMixin, ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario_user.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Funcionario
    fields = ["nome", "departamentos", "empresa"]
    template_name = "funcionarios/funcionario_update_form.html"
    success_url = reverse_lazy('funcionarios:list')
    template_name_suffix = "_update_form"


class FuncionarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios:list')
    template_name = "funcionarios/funcionario_confirm_delete.html"


    def form_valid(self, form):
        if self.verificar_se_pode_deletar():
            messages.success(self.request, 'O funcionário foi deletado com sucesso!')
            return super().form_valid(form)
        else:
            return HttpResponse('Funcionário não pode ser excluidos', status=403)

    def verificar_se_pode_deletar(self):
        funcionario = self.get_object()
        usuario_logado = self.request.user.funcionario_user
        if funcionario.empresa == usuario_logado.empresa and funcionario != usuario_logado:
            return True
        return False
