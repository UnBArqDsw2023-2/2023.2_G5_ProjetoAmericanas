# Generated by Django 4.2.7 on 2023-11-30 01:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('americanas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=40, primary_key=True, serialize=False)),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_pedido', models.DateField()),
                ('status_pedido', models.CharField(max_length=100)),
                ('detalhes_pedido', models.CharField(max_length=100)),
                ('preco_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField()),
                ('estoque', models.IntegerField()),
                ('produto', models.OneToOneField(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, to='americanas.usuario')),
            ],
            options={
                'db_table': 'pedido',
            },
        ),
    ]