# Generated by Django 3.2 on 2021-06-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_project_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img2',
            field=models.ImageField(blank=True, upload_to='img/project', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img3',
            field=models.ImageField(blank=True, upload_to='img/project', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img4',
            field=models.ImageField(blank=True, upload_to='img/project', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img5',
            field=models.ImageField(blank=True, upload_to='img/project', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img6',
            field=models.ImageField(blank=True, upload_to='img/project', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img7',
            field=models.ImageField(blank=True, upload_to='img/project', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img8',
            field=models.ImageField(blank=True, upload_to='img/project', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img9',
            field=models.ImageField(blank=True, upload_to='img/project', verbose_name='Изображение'),
        ),
    ]