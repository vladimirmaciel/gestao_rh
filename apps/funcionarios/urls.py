
from django.urls import path
from  .views import home

app_name = 'funcionarios'
urlpatterns = [
    path('', home, name='home'),
]