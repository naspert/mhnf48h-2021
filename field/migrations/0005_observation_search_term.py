# Generated by Django 2.2 on 2021-05-23 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('field', '0004_auto_20210519_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='search_term',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
