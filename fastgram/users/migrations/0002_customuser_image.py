# Generated by Django 3.2.16 on 2022-12-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='previews/%Y/%m/%d', verbose_name='изображение'),
        ),
    ]
