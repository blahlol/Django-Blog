# Generated by Django 3.0.8 on 2020-07-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='approved',
            field=models.BooleanField(),
        ),
    ]