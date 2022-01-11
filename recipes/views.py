from django.shortcuts import redirect, render
from .models import Recipe
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url="/accounts/login/")
def recipeHome(request):
    recipes = Recipe.objects.all().order_by('date')
    return render(request, 'recipeHome.html', {'recipes':recipes})

@login_required(login_url="/accounts/login/")
def recipe(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    query_pk_and_slug = True
    return render(request, 'recipes/recipe_details.html', {'recipe':recipe})

@login_required(login_url="/accounts/login/")
def create_recipe(request):
    if request.method == 'POST':
        form = forms.CreateRecipe(request.POST,request.FILES)
        if form.is_valid():
            #save form to DB
            temp = form.save(commit=False)
            temp.author = request.user
            temp.save()
            return redirect('recipes:recipeHome')
    else:
        form = forms.CreateRecipe()
    return render(request, 'recipes/recipeCreate.html', {'form':form})
