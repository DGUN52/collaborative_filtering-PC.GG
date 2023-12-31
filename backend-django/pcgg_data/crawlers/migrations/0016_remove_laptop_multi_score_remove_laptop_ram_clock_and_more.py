# Generated by Django 4.2.5 on 2023-10-05 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0015_laptop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='multi_score',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='ram_clock',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='single_score',
        ),
        migrations.AddField(
            model_name='laptop',
            name='manufacturer',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='battery',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='refresh_rate',
            field=models.IntegerField(default=60, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='screen_size',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='thunderbolt',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='usb_a',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='usb_c',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterModelTable(
            name='laptop',
            table='laptop',
        ),
    ]
