# Generated by Django 4.2.1 on 2023-08-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0002_remove_transfer_numberpeople_transfer_adultnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='adultnumber',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=1, verbose_name='Yetişkin'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='childrennumber',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=1, verbose_name='Çocuk'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='fromwhere',
            field=models.CharField(choices=[('Deneme1', 'Deneme1'), ('Deneme2', 'Deneme2'), ('Deneme3', 'Deneme3')], default='-----', max_length=7, verbose_name='Nereden'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='towhere',
            field=models.CharField(choices=[('Deneme1', 'Deneme1'), ('Deneme2', 'Deneme2'), ('Deneme3', 'Deneme3')], default='-----', max_length=7, verbose_name='Nereye'),
        ),
    ]
