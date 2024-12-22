from django.urls import path
from .views import DepartamentoListView

app_name = 'departamentos'

urlpatterns = [
    path('', DepartamentoListView.as_view(), name='list'),
]

