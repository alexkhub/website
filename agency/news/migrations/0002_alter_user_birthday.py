# Generated by Django 4.1.6 on 2023-04-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]
