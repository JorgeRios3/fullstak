# Generated by Django 3.0.8 on 2020-08-08 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0002_auto_20200808_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='viajes.Persona'),
        ),
    ]
