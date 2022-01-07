from django.shortcuts import render
from .models import Recipe
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login/")
def recipeHome(request):
    recipes = Recipe.objects.all().order_by('date')
    return render(request, 'recipeHome.html', {'recipes':recipes})

@login_required(login_url="/accounts/login/")
def recipe(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    return render(request, 'recipes/recipe_details.html', {'recipe':recipe})

@login_required(login_url="/accounts/login/")
def create_recipe(request):
    return render(request, 'recipes/recipeCreate.html')
