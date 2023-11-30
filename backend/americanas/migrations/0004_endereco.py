# Generated by Django 4.2.7 on 2023-11-30 02:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('americanas', '0003_rename_produto_pedido_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=40, primary_key=True, serialize=False)),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
                ('rua', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
                ('complemento', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('estado', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'endereco',
            },
        ),
    ]
