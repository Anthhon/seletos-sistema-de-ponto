# Generated by Django 4.1.1 on 2022-10-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_alter_funcionario_endereço'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='CPF',
            field=models.IntegerField(max_length=11),
        ),
    ]
