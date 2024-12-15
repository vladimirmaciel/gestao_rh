# Generated by Django 5.1.4 on 2024-12-14 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
        ('funcionarios', '0002_alter_funcionario_departamentos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='pertence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='documento_funcionario', to='funcionarios.funcionario'),
            preserve_default=False,
        ),
    ]