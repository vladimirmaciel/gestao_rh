from django.db import models
from funcionarios.models import Funcionairo
import uuid



class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    # owner = models.ForeignKey(Funcionairo, on_delete=models.SET_NULL, null=True,blank=True)
    owner = models.ForeignKey(Funcionairo, on_delete=models.PROTECT)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    
    def  __str__(self):
        return self.descricao
    