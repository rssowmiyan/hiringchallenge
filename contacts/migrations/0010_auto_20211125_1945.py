# Generated by Django 3.2.9 on 2021-11-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_alter_contactinfo_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='ctc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='employees',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
