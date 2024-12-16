
from django.urls import path
from .views import home, FuncionarioCreate, ListFuncionariosView

app_name = 'funcionarios'
urlpatterns = [
    path('', ListFuncionariosView.as_view(), name='list'),
    path('create/', FuncionarioCreate.as_view(), name='create'),
]