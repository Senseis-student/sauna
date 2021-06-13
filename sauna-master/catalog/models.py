from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    categories = (
        ('R', 'Готовые решения'),
        ('O', 'Товары под заказ'),
    )
    title = models.CharField('Название категории', max_length=50)
    categories_type = models.CharField('Раздел категории', choices=categories, max_length=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    title = models.CharField('Название товара', max_length=80)
    description = models.TextField('Описание товара')
    price = models.IntegerField('Цена товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField('Изображение', upload_to='img/product/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'