# Generated by Django 3.2.9 on 2021-11-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_addedpk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='ctc',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='date_of_incorporation',
            field=models.DateField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='employees',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='passing_year',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
