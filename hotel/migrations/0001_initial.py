# Generated by Django 5.0.5 on 2024-05-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('SOLTEIRO', 'Solteiro'), ('CASAL', 'Casal'), ('CONFORT', 'Confort'), ('LUXO', 'Luxo')], max_length=50)),
                ('disponibilidade', models.IntegerField(max_length=3)),
                ('valor', models.FloatField(max_length=4)),
                ('descricao', models.TextField(max_length=255)),
            ],
        ),
    ]