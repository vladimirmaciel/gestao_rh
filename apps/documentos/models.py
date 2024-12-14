from django.db import models

class Documentos(models.Model):
    descricao = models.CharField(max_length=100, help_text='Descrição do documento')


    def __str__(self):
        return self.descricao
