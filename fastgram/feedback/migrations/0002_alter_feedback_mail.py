# Generated by Django 3.2.16 on 2022-12-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='mail',
            field=models.EmailField(help_text='Максимум 254 символа', max_length=254, verbose_name='почта'),
        ),
    ]
