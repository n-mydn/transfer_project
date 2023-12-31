# Generated by Django 4.2.1 on 2023-08-17 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0005_alter_transfer_adultnumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FromWhere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='ToWhere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('fromwhere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.fromwhere', verbose_name='Nereden')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('max_people', models.IntegerField(verbose_name='MaxPeople')),
                ('capasity', models.CharField(choices=[('1-3 Kişi', '1-3 Kişi'), ('1-6 Kişi', '1-6 Kişi'), ('1-13 Kişi', '1-13 Kişi')], max_length=10, verbose_name='Kapasite')),
                ('price', models.IntegerField(verbose_name='Ücret')),
                ('currency', models.CharField(blank=True, default='TRY', max_length=3, verbose_name='Birim')),
                ('car_image', models.FileField(upload_to='', verbose_name='Resim')),
                ('fromwhere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.fromwhere', verbose_name='Nereden')),
                ('towhere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.towhere', verbose_name='Nereye')),
            ],
        ),
        migrations.AlterField(
            model_name='transfer',
            name='fromwhere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.fromwhere', verbose_name='Nereden'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='fromwhere_de',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.fromwhere', verbose_name='Nereden'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='fromwhere_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.fromwhere', verbose_name='Nereden'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='fromwhere_tr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.fromwhere', verbose_name='Nereden'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='towhere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.towhere', verbose_name='Nereye'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='towhere_de',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.towhere', verbose_name='Nereye'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='towhere_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.towhere', verbose_name='Nereye'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='towhere_tr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.towhere', verbose_name='Nereye'),
        ),
    ]
