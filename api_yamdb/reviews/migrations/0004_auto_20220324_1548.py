# Generated by Django 2.2.16 on 2022-03-24 10:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220324_0022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Оценка должна быть не меньше 1'), django.core.validators.MaxValueValidator(10, message='Оценка должна быть не больше 10')]),
        ),
    ]
