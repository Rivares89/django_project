# Generated by Django 5.0 on 2024-01-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='current',
            field=models.BooleanField(default=False, verbose_name='признак текущей версии'),
        ),
    ]
