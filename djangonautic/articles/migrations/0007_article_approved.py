# Generated by Django 3.0.8 on 2020-07-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200730_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='approved',
            field=models.BooleanField(default=None),
        ),
    ]