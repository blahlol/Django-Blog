# Generated by Django 3.0.8 on 2020-07-30 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200730_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
    ]
