
from django.urls import path
from .views import home, FuncionarioCreate

app_name = 'funcionarios'
urlpatterns = [
    path('', home, name='home'),
    path('create/', FuncionarioCreate.as_view(), name='create'),
]