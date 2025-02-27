# Generated by Django 5.1.6 on 2025-02-21 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('I', 'In Progress'), ('R', 'Ready'), ('D', 'Delivered')], default='P', max_length=1)),
                ('burger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OSM.burger')),
            ],
        ),
    ]
