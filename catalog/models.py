from django.db import models

NULLABLE = {'blank': True, 'null': True}
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    price_for_one = models.CharField(max_length=100, verbose_name='цена за штуку')
    date_creation = models.CharField(max_length=100, verbose_name='дата создания')
    last_modified_data = models.CharField(max_length=100, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)

class Category(models.Model):
    name_c = models.CharField(max_length=100, verbose_name='название', default='DEFAULT VALUE')
    description_c = models.CharField(max_length=100, verbose_name='описание', default='DEFAULT VALUE')

    def __str__(self):
        return f'{self.name_c} {self.description_c}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name_c',)
