from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.departamentos.models import Departamento


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
    fields = ['nome']
    template_name = 'departamentos/departamento_form.html'
    success_url = '/departamentos/'

    # def get_form(self, form_class=None):
    #     # Obtém o formulário padrão
    #     form = super().get_form(form_class)
    #
    #     # Filtra o campo 'empresa' para mostrar apenas a empresa do usuário logado
    #     funcionario = self.request.user.funcionario_user
    #     form.fields['empresa'].queryset = Empresa.objects.filter(id=funcionario.empresa.id)
    #
    #     return form

    def form_valid(self, form):
        obj_departamento = form.save(commit=False)
        obj_departamento.empresa = self.request.user.funcionario_user.empresa
        obj_departamento.save()
        return super(CreateDepartamentoView, self).form_valid(form)


class UpateDepartamentoView(LoginRequiredMixin, UpdateView):
    model = Departamento
    fields = ['nome','is_active']
    template_name = 'departamentos/departamento_update_form.html'
    success_url = '/departamentos/'

    def form_valid(self, form):
        obj_departamento = form.save(commit=False)
        obj_departamento.empresa = self.request.user.funcionario_user.empresa
        obj_departamento.save()
        return super(UpateDepartamentoView, self).form_valid(form)

class DeleteDepartamentoView(LoginRequiredMixin, DeleteView):
    model = Departamento
    template_name = 'departamentos/departamento_delete_confirm.html'
    success_url = '/departamentos/'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.is_active = False
        obj.save()
        return super(DeleteDepartamentoView, self).delete(request, *args, **kwargs)
