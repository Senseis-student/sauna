from django.db import models


class Wood(models.Model):
    title = models.CharField('Название дерева', max_length=100)
    img = models.ImageField('Изображение', upload_to='img/wood')
    categories = (
        ('V', 'Вагонка'),
        ('P', 'Полок'),
    )
    categories_type = models.CharField('Тип', choices=categories, max_length=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дерево'
        verbose_name_plural = 'Дерево'

class Options(models.Model):
    title = models.CharField('Наименование опции', max_length=100)
    img = models.ImageField('Изображение', upload_to='img/options')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опция'
        verbose_name_plural = 'Опции'

class Form(models.Model):
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание заявки', blank=True)
    scale = models.CharField('Размер помещения', max_length=50)
    sity = models.CharField('Город', max_length=200)
    village = models.CharField('Расположение объекта от города', max_length=100)
    number = models.CharField('Номер телефона', max_length=15)
    email = models.EmailField('Почта', max_length=150)
    img = models.ImageField('Изображение', upload_to='img/proposal', blank=True)
    form_wood = models.ManyToManyField(Wood)  
    form_options = models.ManyToManyField(Options)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Зявка'
        verbose_name_plural = 'Заявки'

