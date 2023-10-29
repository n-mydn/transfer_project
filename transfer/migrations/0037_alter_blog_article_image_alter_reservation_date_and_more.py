# Generated by Django 4.2.1 on 2023-10-06 12:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0036_blog_alter_reservation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Başlık Fotoğrafı'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=datetime.date(2023, 10, 6), verbose_name='Transfer Tarihi'),
        ),
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromwhere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.fromwhere', verbose_name='Nereden')),
                ('towhere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.towhere', verbose_name='Nereye')),
            ],
        ),
    ]
