# Generated by Django 3.0.8 on 2020-07-31 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20200731_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]