# Generated by Django 5.0.5 on 2024-05-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_usuario_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='quartos',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]