# Generated by Django 2.2.24 on 2021-12-28 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('difficulty', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], max_length=1)),
                ('date', models.DateField(auto_now_add=True)),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient')),
            ],
        ),
    ]