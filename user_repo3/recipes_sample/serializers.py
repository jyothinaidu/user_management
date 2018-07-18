from rest_framework import serializers
from .models import *


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishDetails
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'


class RiseIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiseIngredients
        fields = '__all__'


class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = '__all__'


class RecipesSerializer(serializers.ModelSerializer):
    recipe_assets = AssetsSerializer(many=True, read_only=True)
    recipe_categories = CategorySerializer(many=True, read_only=True)
    recipe_dishes = DishSerializer(many=True, read_only=True)
    recipe_ingredients = IngredientSerializer(many=True, read_only=True)
    recipe_rise_ingredients = RiseIngredientSerializer(many=True, read_only=True)
    recipe_taxonomy = TaxonomySerializer(many=True, read_only=True)
    # recipe_assets = serializers.SlugRelatedField(queryset=Assets.objects.all())

    class Meta:
        model = Recipes
        fields = (
            'recipeid',
            'recipe_assets',
            'appid',
            'recipeSource',
            'recipeTitle',
            'recipedesc',
            'recipeimage',
            'recipe_categories',
            'recipe_dishes',
            'recipe_ingredients',
            'recipe_rise_ingredients',
            'recipe_taxonomy',
        )


class RecipeMealplanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeMealplans
        fields = '__all__'


class MealplanSerializer(serializers.ModelSerializer):
    recipes_mealplan = RecipeMealplanSerializer(many=True, read_only=True)
    mealplan_rid = RecipesSerializer(many=True, read_only=True)

    class Meta:
        model = Mealplans
        fields = (
            'MealId',
            'MealName',
            'AppId',
            'recipes_mealplan',
            'mealplan_rid',
        )


