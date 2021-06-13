from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from proposal.models import Options


class Project(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    leader = models.CharField('Руководитель проекта', max_length=50, blank=True)
    designer = models.CharField('Дизайнер', max_length=50, blank=True)
    plotnik = models.CharField('Плотник', max_length=50, blank=True)
    city = models.CharField('Город', max_length=150, blank=True)
    scale = models.CharField('Размер', max_length=50, blank=True)
    price = models.CharField('Итоговая стоимость', max_length=50, blank=True)
    link = models.URLField('Ссылка на видео', blank=True)
    main_img = models.ImageField('Главное изображение', upload_to='img/project')
    img2 = models.ImageField('Изображение', upload_to='img/project', blank=True)
    img3 = models.ImageField('Изображение', upload_to='img/project', blank=True)
    img4 = models.ImageField('Изображение', upload_to='img/project', blank=True)
    img5 = models.ImageField('Изображение', upload_to='img/project', blank=True)
    img6 = models.ImageField('Изображение', upload_to='img/project', blank=True)
    img7 = models.ImageField('Изображение', upload_to='img/project', blank=True)
    img8 = models.ImageField('Изображение', upload_to='img/project', blank=True)
    img9 = models.ImageField('Изображение', upload_to='img/project', blank=True)
    project_options = models.ManyToManyField(Options)

    def __str__(self):
        return self.title

    def img_list(self):
        return [self.img2, self.img3, self.img4, self.img5, self.img6]

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
