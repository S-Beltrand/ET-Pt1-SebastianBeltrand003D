# Generated by Django 3.2.4 on 2021-07-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='montoPago',
            field=models.IntegerField(default=3, verbose_name='Precio base'),
            preserve_default=False,
        ),
    ]
