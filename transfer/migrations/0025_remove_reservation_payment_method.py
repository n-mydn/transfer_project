# Generated by Django 4.2.1 on 2023-09-07 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0024_remove_reservation_bill_mail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='payment_method',
        ),
    ]
