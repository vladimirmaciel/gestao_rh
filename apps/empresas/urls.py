from django.urls import path
from .views import EmpresaCreateView, EmpresaEditView, EmpresaListView

app_name = 'empresas'

urlpatterns = [
    path('create/', EmpresaCreateView.as_view(), name='create'),
    path('update/<int:pk>/', EmpresaEditView.as_view(), name='update'),
    path('', EmpresaListView.as_view(), name='list'),
]

