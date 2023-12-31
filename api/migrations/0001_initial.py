# Generated by Django 3.2 on 2023-06-27 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlturaReservorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_a', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tiempo_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bomba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_inicio', models.DateTimeField()),
                ('tiempo_final', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HumedadReservorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_h', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tiempo_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254)),
                ('nombre_usuario', models.CharField(max_length=200)),
                ('contraseña', models.CharField(max_length=200)),
            ],
        ),
    ]
