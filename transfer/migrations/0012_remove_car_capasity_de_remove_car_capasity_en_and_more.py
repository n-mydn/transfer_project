# Generated by Django 4.2.1 on 2023-08-17 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0011_car_capasity_de_car_capasity_en_car_capasity_tr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='capasity_de',
        ),
        migrations.RemoveField(
            model_name='car',
            name='capasity_en',
        ),
        migrations.RemoveField(
            model_name='car',
            name='capasity_tr',
        ),
        migrations.RemoveField(
            model_name='car',
            name='currency_de',
        ),
        migrations.RemoveField(
            model_name='car',
            name='currency_en',
        ),
        migrations.RemoveField(
            model_name='car',
            name='currency_tr',
        ),
        migrations.RemoveField(
            model_name='car',
            name='fromwhere_de',
        ),
        migrations.RemoveField(
            model_name='car',
            name='fromwhere_en',
        ),
        migrations.RemoveField(
            model_name='car',
            name='fromwhere_tr',
        ),
        migrations.RemoveField(
            model_name='car',
            name='name_de',
        ),
        migrations.RemoveField(
            model_name='car',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='car',
            name='name_tr',
        ),
        migrations.RemoveField(
            model_name='car',
            name='price_de',
        ),
        migrations.RemoveField(
            model_name='car',
            name='price_en',
        ),
        migrations.RemoveField(
            model_name='car',
            name='price_tr',
        ),
        migrations.RemoveField(
            model_name='car',
            name='towhere_de',
        ),
        migrations.RemoveField(
            model_name='car',
            name='towhere_en',
        ),
        migrations.RemoveField(
            model_name='car',
            name='towhere_tr',
        ),
    ]
