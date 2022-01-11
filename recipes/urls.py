from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipeHome, name="recipeHome"),
    path('create/', views.create_recipe, name='create'),
    path('<slug:slug>/', views.recipe, name="recipePage")
]
