# Generated by Django 4.2.5 on 2023-09-25 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0012_rename_max_cooler_width_case_max_cooler_depth_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='case',
            table='part_chassis',
        ),
    ]
