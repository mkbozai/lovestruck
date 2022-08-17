# Generated by Django 4.1 on 2022-08-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_location_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='reservation',
        ),
        migrations.AlterField(
            model_name='date',
            name='budget',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='date',
            name='rating',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]