# Generated by Django 5.1.2 on 2024-12-03 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('rfc', models.CharField(max_length=15)),
                ('cuenta', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('sexo', models.CharField(max_length=10)),
                ('edad', models.SmallIntegerField()),
            ],
        ),
    ]
