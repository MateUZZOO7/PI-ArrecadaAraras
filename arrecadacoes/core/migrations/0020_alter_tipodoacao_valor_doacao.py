# Generated by Django 5.0.4 on 2024-06-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_rename_valor_tipodoacao_valor_doacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodoacao',
            name='valor_doacao',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]