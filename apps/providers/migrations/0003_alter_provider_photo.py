# Generated by Django 4.2 on 2023-04-18 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='providers'),
        ),
    ]
