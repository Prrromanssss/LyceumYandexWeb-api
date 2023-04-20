# Generated by Django 3.2.16 on 2022-12-21 06:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='subject_type_from',
            field=models.PositiveSmallIntegerField(choices=[('1', 'город федерального значения'), ('2', 'республика'), ('3', 'край'), ('4', 'область'), ('5', 'автономный округ'), ('6', 'автономная область')], default='1', verbose_name='Тип субъекта'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='subject_type_to',
            field=models.PositiveSmallIntegerField(choices=[('1', 'город федерального значения'), ('2', 'республика'), ('3', 'край'), ('4', 'область'), ('5', 'автономный округ'), ('6', 'автономная область')], default='1', verbose_name='Тип субъекта'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='city_from',
            field=models.CharField(help_text='Максимум 50 символов', max_length=50, verbose_name='Город отправки посылки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='city_to',
            field=models.CharField(help_text='Максимум 50 символов', max_length=50, verbose_name='Город получения посылки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='district_from',
            field=models.CharField(blank=True, default='', help_text='Максимум 50 символов', max_length=50, verbose_name='Округ отправки посылки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='district_to',
            field=models.CharField(blank=True, default='', help_text='Максимум 50 символов', max_length=50, verbose_name='Округ получения посылки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='height',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)], verbose_name='высота'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='length',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)], verbose_name='длина'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='subject_from',
            field=models.CharField(help_text='Введите только название субъекта, максимум 50 символов', max_length=50, verbose_name='Субъект РФ отправки посылки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='subject_to',
            field=models.CharField(help_text='Введите только название субъекта, максимум 50 символов', max_length=50, verbose_name='Субъект РФ получения посылки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='weight',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='вес'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='width',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(80)], verbose_name='ширина'),
        ),
    ]