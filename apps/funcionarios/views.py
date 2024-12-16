from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from apps.funcionarios.models import Funcionario


def home(request):
    return HttpResponse('Olá mundo!')


class FuncionarioCreate(LoginRequiredMixin,CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos', 'empresa']
    template_name = 'funcionarios/funcionario_form.html'
    success_url = reverse_lazy('funcionarios:list')

    def get_success_url(self):
        return super().get_success_url()

class ListFuncionariosView(LoginRequiredMixin,ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario_user.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ["nome", "departamentos", "empresa"]
    template_name = "funcionarios/funcionario_update_form.html"
    success_url = reverse_lazy('funcionarios:list')
    template_name_suffix = "_update_form"
