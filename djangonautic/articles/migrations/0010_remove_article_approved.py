# Generated by Django 3.0.8 on 2020-07-31 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20200731_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='approved',
        ),
    ]