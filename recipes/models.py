from enum import auto, unique
from typing import DefaultDict
from typing_extensions import NotRequired
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, AutoField, CharField, SlugField
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
from Cravings.utils import unique_slug_generator

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    about = models.TextField(blank=True, max_length=300)
    ingredients = models.ManyToManyField(Ingredient)
    TIME_CHOICES = (
        ('0-10 mins', '0-10 mins'),
        ('12-25 mins', '10-25 mins'),
        ('25-40 mins', '25-40 mins'),
        ('40+ mins', '40+ mins')
    )
    # cooking_time = models.CharField(blank=True, max_length=20, choices=TIME_CHOICES)
    photo = models.ImageField(default='default.jpg', blank=True)
    # servings = models.PositiveSmallIntegerField(blank=True)
    procedure = models.TextField(blank=True)
    DIFFICULTY_CHOICES = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    )
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    favourite = models.BooleanField(default=False)
    bookmark = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

def slug_generator(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Recipe)

    # def get_absolute_url(self):
    #     return reverse('article_detail', kwargs={'slug': self.slug})

