from django.urls import path
from .views import DepartamentoListView, CreateDepartamentoView, UpateDepartamentoView, DeleteDepartamentoView

app_name = 'departamentos'

urlpatterns = [
    path('', DepartamentoListView.as_view(), name='list'),
    path('create/', CreateDepartamentoView.as_view(), name='create'),
    path('update/<int:pk>/', UpateDepartamentoView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteDepartamentoView.as_view(), name='delete'),
]

