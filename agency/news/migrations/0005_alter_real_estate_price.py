# Generated by Django 4.1.7 on 2023-05-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_real_estate_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='real_estate',
            name='price',
            field=models.IntegerField(verbose_name='цена'),
        ),
    ]