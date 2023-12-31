# Generated by Django 4.2.1 on 2023-09-14 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0034_remove_reservation_mail_context_reservation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='extras',
            name='price_de',
            field=models.IntegerField(null=True, verbose_name='Ücret'),
        ),
        migrations.AddField(
            model_name='extras',
            name='price_en',
            field=models.IntegerField(null=True, verbose_name='Ücret'),
        ),
        migrations.AddField(
            model_name='extras',
            name='price_tr',
            field=models.IntegerField(null=True, verbose_name='Ücret'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=datetime.date(2023, 9, 14), verbose_name='Transfer Tarihi'),
        ),
    ]
