# Generated by Django 2.2.24 on 2021-12-29 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20211228_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='about',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
