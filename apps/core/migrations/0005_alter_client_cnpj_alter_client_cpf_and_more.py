# Generated by Django 4.0.4 on 2022-07-16 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_alter_client_bairro_alter_client_celular_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='data_aniversario',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='desconto',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
