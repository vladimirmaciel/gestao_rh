# Generated by Django 4.0.5 on 2022-06-14 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_funcionairo_departamentos_funcionairo_empresa_and_more'),
        ('documentos', '0002_documento_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionairo'),
            preserve_default=False,
        ),
    ]
