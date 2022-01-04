from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipeHome, name="recipeHome"),
    path('<slug:slug>', views.recipe, name="recipePage")
]
