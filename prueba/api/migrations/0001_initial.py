# Generated by Django 3.2.7 on 2021-09-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('edad', models.IntegerField(max_length=5)),
                ('email', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
    ]
