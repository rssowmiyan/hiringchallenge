# Generated by Django 3.2.9 on 2021-11-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0011_alter_contactinfo_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='ctc',
            field=models.CharField(max_length=10),
        ),
    ]
