# Generated by Django 3.0.4 on 2020-03-15 02:05

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20200315_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
