# Generated by Django 3.2 on 2021-06-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание заявки'),
        ),
        migrations.AlterField(
            model_name='form',
            name='email',
            field=models.EmailField(max_length=150, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='form',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/proposal', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='form',
            name='number',
            field=models.CharField(max_length=15, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='form',
            name='scale',
            field=models.CharField(max_length=50, verbose_name='Размер помещения'),
        ),
    ]