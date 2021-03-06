# Generated by Django 4.0.4 on 2022-07-24 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_alter_client_cnpj_alter_client_cpf_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Aberto', 'Aberto'), ('Fechado', 'Fechado'), ('Cancelado', 'Cancelado')], default='Aberto', max_length=50)),
                ('dentista', models.CharField(blank=True, max_length=255, null=True)),
                ('instituicao', models.CharField(blank=True, max_length=255, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.client')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
