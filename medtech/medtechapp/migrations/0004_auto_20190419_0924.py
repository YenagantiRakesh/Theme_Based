# Generated by Django 2.0.1 on 2019-04-19 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medtechapp', '0003_auto_20190419_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remedies',
            name='ingredients',
            field=models.CharField(max_length=300),
        ),
    ]
