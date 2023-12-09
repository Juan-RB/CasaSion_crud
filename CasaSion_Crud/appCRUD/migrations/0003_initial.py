# Generated by Django 4.2.5 on 2023-11-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appCRUD', '0002_delete_usuariocrud'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioCRUD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('rut', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('comuna', models.CharField(max_length=40)),
            ],
        ),
    ]
