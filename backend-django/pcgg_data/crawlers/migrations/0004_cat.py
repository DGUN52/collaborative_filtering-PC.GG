# Generated by Django 4.2.5 on 2023-09-18 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0003_alter_pricehistory_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
