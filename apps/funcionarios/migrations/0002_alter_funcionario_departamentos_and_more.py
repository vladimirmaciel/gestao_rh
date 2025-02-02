# Generated by Django 5.1.4 on 2024-12-14 22:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
        ('empresas', '0001_initial'),
        ('funcionarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='departamentos',
            field=models.ManyToManyField(related_name='funcionario_departamento', to='departamentos.departamento'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='funcionario_empresa', to='empresas.empresa'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='funcionario_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
