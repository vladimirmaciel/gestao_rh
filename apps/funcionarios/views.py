from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from apps.funcionarios.models import Funcionario


def home(request):
    return HttpResponse('Olá mundo!')


class FuncionarioCreate(LoginRequiredMixin,CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos', 'empresa']
    template_name = 'funcionarios/funcionario_form.html'
    success_url = reverse_lazy('funcionarios:funcionario_list')

    def get_success_url(self):
        return super().get_success_url()
