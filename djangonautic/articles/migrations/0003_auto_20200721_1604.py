# Generated by Django 3.0.8 on 2020-07-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='no_of_likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
