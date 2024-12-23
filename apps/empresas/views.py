from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from .models import Empresa


class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = 'empresas/empresa_list.html'
    context_object_name = 'empresas'  # Nome do objeto que será passado para o template

    def get_queryset(self):
        funcionario = self.request.user.funcionario_user

        return Empresa.objects.filter(funcionario_empresa=funcionario)


class EmpresaCreateView(LoginRequiredMixin, CreateView):
    model = Empresa
    fields = ['nome']  # Exemplo de campos
    template_name = 'empresas/empresa_form.html'
    success_url = '/empresas/'  # Redirecionar após criação

    def form_valid(self, form):
        obj_empresa = form.save()
        # funcionario = self.request.user.funcionario_user
        # funcionario.empresa = obj_empresa
        # funcionario.save()
        return HttpResponse('Empresa criada com sucesso!')  # Exemplo de retorno


class EmpresaEditView(LoginRequiredMixin, UpdateView):
    model = Empresa
    fields = ['nome']  # Exemplo de campos
    template_name = 'empresas/empresa_form.html'
    success_url = reverse_lazy('core:home')  # Redirecionar após edição# Exemplo de redirecionamento

    def form_valid(self, form):
        # Adiciona uma mensagem de sucesso
        messages.success(self.request, 'A empresa foi alterada com sucesso!')
        return super().form_valid(form)
