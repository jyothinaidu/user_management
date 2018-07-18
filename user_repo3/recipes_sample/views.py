from django.shortcuts import render
from rest_framework import viewsets, views, generics
from .models import *
from .serializers import *

from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter


class AssetsView(generics.ListCreateAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer
    name = 'Assets-List'


class AssetsDetailView(generics.RetrieveDestroyAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer
    name = 'Assets-Detail'


class CategoryView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    name = 'Categories-List'


class CategoryDetailView(generics.RetrieveDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    name = 'Categories-Detail'


class DishView(generics.ListCreateAPIView):
    queryset = DishDetails.objects.all()
    serializer_class = DishSerializer
    name = 'Dishes-List'


class DishDetailView(generics.RetrieveDestroyAPIView):
    queryset = DishDetails.objects.all()
    serializer_class = DishSerializer
    name = 'Dishes-Detail'


class IngredientView(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    name = 'Ingredients-List'


class IngredientDetailView(generics.RetrieveDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    name = 'Ingredients-detail'


class RiseIngredientView(generics.ListCreateAPIView):
    queryset = RiseIngredients.objects.all()
    serializer_class = RiseIngredientSerializer
    name = 'RiseIngredients-list'


class RiseIngredientDetailView(generics.RetrieveDestroyAPIView):
    queryset = RiseIngredients.objects.all()
    serializer_class = RiseIngredientSerializer
    name = 'RiseIngredients-detail'


class TaxonomyView(generics.ListCreateAPIView):
    queryset = Taxonomy.objects.all()
    serializer_class = TaxonomySerializer
    name = 'Taxonomy-List'


class TaxonomyDetailView(generics.RetrieveDestroyAPIView):
    queryset = Taxonomy.objects.all()
    serializer_class = TaxonomySerializer
    name = 'Taxonomy-detail'


class RecipesView(generics.ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    name = 'Recipes-List'
    filter_fields = (
        'recipeid',
    )


class RecipesDetailView(generics.RetrieveDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    name = 'Recipes-Detail'


class RecipeMealPlanView(generics.ListCreateAPIView):
    queryset = RecipeMealplans.objects.all()
    serializer_class = RecipeMealplanSerializer
    name = 'Recipes-meal_plan-List'


class RecipeMealPlanDetailView(generics.RetrieveDestroyAPIView):
    queryset = RecipeMealplans.objects.all()
    serializer_class = RecipeMealplanSerializer
    name = 'Recipes-meal_plan-Detail'


class MealplanView(generics.ListCreateAPIView):
    queryset = Mealplans.objects.all()
    serializer_class = MealplanSerializer
    name = 'Meal_Plan-List'


class MealplanDetailView(generics.RetrieveDestroyAPIView):
    queryset = Mealplans.objects.all()
    serializer_class = MealplanSerializer
    name = 'Meal_Plan-Detail'
