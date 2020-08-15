# Generated by Django 3.0.8 on 2020-08-08 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='viajes.Persona'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido_paterno',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]