# Generated by Django 3.2.9 on 2021-12-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
