from django.db import models
import uuid



class Departamento(models.Model):
    nome = models.CharField(max_length=70)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    
    def  __str__(self):
        return self.nome