# Generated by Django 5.0.4 on 2024-06-12 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_cliente_remove_doacao_quantidade_doada_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastromodel',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='cadastromodel',
            name='data_nasc',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='data_nasc',
        ),
    ]