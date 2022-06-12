from django.db import models
import uuid



class Empresa(models.Model):
    nome = models.CharField(max_length=100,help_text="Nome da empresa")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    