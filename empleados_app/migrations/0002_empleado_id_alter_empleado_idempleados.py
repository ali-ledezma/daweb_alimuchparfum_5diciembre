# Generated by Django 5.1.2 on 2024-12-05 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='idempleados',
            field=models.IntegerField(),
        ),
    ]