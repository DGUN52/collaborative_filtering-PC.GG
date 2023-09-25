# Generated by Django 4.2.5 on 2023-09-25 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0014_rename_start_date_pricehistory_changed_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('image_source', models.URLField(null=True)),
                ('extinct', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=20, null=True)),
                ('os', models.CharField(max_length=20, null=True)),
                ('screen_size', models.IntegerField(null=True)),
                ('refresh_rate', models.IntegerField(null=True)),
                ('resolution', models.CharField(max_length=20, null=True)),
                ('brightness', models.IntegerField(null=True)),
                ('cpu', models.CharField(max_length=100, null=True)),
                ('ram_capacity', models.IntegerField(null=True)),
                ('ram_clock', models.IntegerField(null=True)),
                ('ram_upgradeable', models.BooleanField(default=False, null=True)),
                ('gpu', models.CharField(max_length=100, null=True)),
                ('tgp', models.IntegerField(null=True)),
                ('ssd', models.FloatField(null=True)),
                ('cellular', models.BooleanField(default=False, null=True)),
                ('hdmi', models.BooleanField(default=False, null=True)),
                ('thunderbolt', models.IntegerField(null=True)),
                ('usb_a', models.IntegerField(null=True)),
                ('usb_c', models.IntegerField(null=True)),
                ('sd_card', models.CharField(max_length=20, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('battery', models.IntegerField(null=True)),
                ('single_score', models.IntegerField(null=True)),
                ('multi_score', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'part_laptop',
            },
        ),
    ]
