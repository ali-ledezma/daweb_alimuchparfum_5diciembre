# Generated by Django 5.1.2 on 2024-12-03 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
