# Generated by Django 4.2.5 on 2023-09-25 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0013_alter_case_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricehistory',
            old_name='start_date',
            new_name='changed_date',
        ),
        migrations.RemoveField(
            model_name='board',
            name='changed_date',
        ),
        migrations.RemoveField(
            model_name='case',
            name='changed_date',
        ),
        migrations.RemoveField(
            model_name='cooler',
            name='changed_date',
        ),
        migrations.RemoveField(
            model_name='cpu',
            name='changed_date',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='changed_date',
        ),
        migrations.RemoveField(
            model_name='power',
            name='changed_date',
        ),
        migrations.RemoveField(
            model_name='pricehistory',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='ram',
            name='changed_date',
        ),
        migrations.RemoveField(
            model_name='ssd',
            name='changed_date',
        ),
    ]