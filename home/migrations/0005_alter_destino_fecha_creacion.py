# Generated by Django 4.1.2 on 2022-10-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_destino_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destino',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
