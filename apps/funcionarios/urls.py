
from django.urls import path
from .views import home, FuncionarioCreate, ListFuncionariosView, FuncionarioUpdateView

app_name = 'funcionarios'
urlpatterns = [
    path('', ListFuncionariosView.as_view(), name='list'),
    path('create/', FuncionarioCreate.as_view(), name='create'),
    path('update/<int:pk>/', FuncionarioUpdateView.as_view(), name='update'),
]