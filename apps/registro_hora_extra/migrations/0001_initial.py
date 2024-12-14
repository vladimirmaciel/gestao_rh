# Generated by Django 5.1.4 on 2024-12-14 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroHoraExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=100)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario')),
            ],
        ),
    ]
