from django.urls import path
from .views import DepartamentoListView, CreateDepartamentoView

app_name = 'departamentos'

urlpatterns = [
    path('', DepartamentoListView.as_view(), name='list'),
    path('create/', CreateDepartamentoView.as_view(), name='create'),
]

