# Generated by Django 5.1.6 on 2025-02-21 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OSM', '0003_alter_pedido_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burger',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
