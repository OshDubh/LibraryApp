# Generated by Django 4.1.5 on 2023-01-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(default='comedy', max_length=64),
        ),
    ]
