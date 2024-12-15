from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Empresa

class EmpresaCreateView(LoginRequiredMixin,CreateView):
    model = Empresa
    fields = ['nome']  # Exemplo de campos
    template_name = 'empresas/empresa_form.html'
    success_url = '/empresas/'  # Redirecionar após criação
