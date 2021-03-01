# Generated by Django 3.1.5 on 2021-02-28 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Livro')),
                ('autor', models.CharField(max_length=50, verbose_name='Autor')),
                ('copias', models.PositiveIntegerField(verbose_name='Cópias em estoque')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_solicitacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da Solicitação')),
                ('dias_reserva', models.PositiveIntegerField(verbose_name='Dias pra reserva')),
                ('data_aprovacao', models.DateTimeField(verbose_name='Data da Aprovação')),
                ('pedido_aprovado', models.BooleanField(default=False, verbose_name='Pedido Aprovado')),
                ('leitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.livro')),
            ],
        ),
    ]
