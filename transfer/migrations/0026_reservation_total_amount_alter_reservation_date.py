# Generated by Django 4.2.1 on 2023-09-09 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0025_remove_reservation_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='total_amount',
            field=models.IntegerField(default=0, verbose_name='Toplam Fiyat'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=datetime.date(2023, 9, 9), verbose_name='Transfer Tarihi'),
        ),
    ]
