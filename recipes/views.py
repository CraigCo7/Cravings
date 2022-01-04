from django.shortcuts import render
from .models import Recipe
from django.http import HttpResponse

# Create your views here.
def recipeHome(request):
    recipes = Recipe.objects.all().order_by('date')
    return render(request, 'recipeHome.html', {'recipes':recipes})

def recipe(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    return render(request, 'recipes/recipe_details.html', {'recipe':recipe})
