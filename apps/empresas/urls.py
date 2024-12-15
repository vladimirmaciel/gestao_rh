from django.urls import path
from .views import EmpresaCreateView

app_name = 'empresas'

urlpatterns = [
    path('create/', EmpresaCreateView.as_view(), name='create'),
]
