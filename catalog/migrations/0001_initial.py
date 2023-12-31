# Generated by Django 5.0 on 2023-12-22 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.CharField(max_length=100, verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение')),
                ('category', models.CharField(max_length=100, verbose_name='категория')),
                ('price_for_one', models.CharField(max_length=100, verbose_name='цена за штуку')),
                ('date_creation', models.CharField(max_length=100, verbose_name='дата создания')),
                ('last_modified_data', models.CharField(max_length=100, verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('name',),
            },
        ),
    ]
