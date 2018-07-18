from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField

import uuid

from datetime import datetime


class Recipes(models.Model):
    recipeid = models.IntegerField(primary_key=True)
    appid = models.IntegerField(default=0, null=True)
    recipeSource = models.CharField(max_length=100, default='null', null=True)
    recipeTitle = models.CharField(max_length=100, default='null', null=True)
    recipedesc = models.CharField(max_length=100, default='null', null=True)
    recipeimage = models.CharField(max_length=100, default='null', null=True)

    class Meta:
        managed = True
        verbose_name_plural = "Recipes"
        db_table = 'recipes'


class Assets(models.Model):
    assetsid = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=100, default='null', null=True)
    imageType = models.CharField(max_length=100, default='null', null=True)
    mimeType = models.CharField(max_length=100, default='null', null=True)
    publicationDate = models.DateField(null=True)
    status = models.IntegerField(default=0, null=True)
    title = models.CharField(max_length=100, default='null', null=True)
    type = models.CharField(max_length=100, default='null', null=True)
    r_assets = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="recipe_assets")

    class Meta:
        managed = True
        verbose_name_plural = "Assets"
        db_table = 'assets'


class Categories(models.Model):
    categoryId = models.IntegerField(primary_key=True)
    categoryName = models.CharField(max_length=100, default='null', null=True)
    categoryRank = models.IntegerField(null=True)
    subcategoryId = models.IntegerField(null=False, unique=True)
    subcategoryName = models.CharField(max_length=100, default='null', null=True)
    subcategoryRank = models.IntegerField(null=True)
    r_categories = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="recipe_categories")

    class Meta:
        managed = True
        verbose_name_plural = "Categories"
        db_table = 'categories'


class DishDetails(models.Model):
    dishId = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=100, default='null', null=True)
    url = models.CharField(max_length=100, default='null', null=True)
    r_dish = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="recipe_dishes")

    class Meta:
        managed = True
        verbose_name_plural = "Dishes"
        db_table = 'dishes'


class Ingredients(models.Model):
    IngredientId = models.IntegerField(primary_key=True)
    FullMeasure = models.CharField(max_length=100, default='null', null=True)
    FullWeight = models.CharField(max_length=100, default='null', null=True)
    IngredientGridHeaders = models.CharField(max_length=100, default='null', null=True)
    IngredientName = models.CharField(max_length=100, default='null', null=True)
    IngredientStep = models.IntegerField(default=0)
    LanguageId = models.IntegerField(default=0)
    PostPreparation = models.CharField(max_length=100, default='null', null=True)
    PrePreparation = models.CharField(max_length=100, default='null', null=True)
    QuantityNum = models.CharField(max_length=100, default='null', null=True)
    QuantityText = models.CharField(max_length=100, default='null', null=True)
    QuantityUnit = models.CharField(max_length=100, default='null', null=True)
    RecipeIngredientID = models.CharField(max_length=100, default='null', null=True)
    TrialMeasure = models.CharField(max_length=100, default='null', null=True)
    TrialWeight = models.CharField(max_length=100, default='null', null=True)
    r_ingredient = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="recipe_ingredients")

    class Meta:
        managed = True
        verbose_name_plural = "Ingredients"
        db_table = 'ingredients'


class RiseIngredients(models.Model):
    IngredientId = models.IntegerField(primary_key=True)
    IngredientCategory = models.CharField(max_length=100, default='null', null=True)
    IngredientIndustrySector = models.CharField(max_length=100, default='null', null=True)
    IngredientType = models.CharField(max_length=100, default='null', null=True)
    ProductId = models.CharField(max_length=100, default='null', null=True)
    r_rise_ingredient = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="recipe_rise_ingredients")

    class Meta:
        managed = True
        verbose_name_plural = "RiseIngredients"
        db_table = 'riseingredients'


class Taxonomy(models.Model):
    TaxonomyId = models.IntegerField(primary_key=True)
    TaxonomyName = models.CharField(max_length=100, default='null', null=True)
    LanguageId = models.IntegerField(default=0, null=True)
    CountryId = models.IntegerField(default=0, null=True)
    InsertDate = models.DateField(null=True)
    Ludate = models.DateField(null=True)
    status = models.CharField(max_length=100, default='null', null=True)
    hierarchy_level = models.IntegerField(null=True)
    r_taxonomy = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="recipe_taxonomy")

    class Meta:
        managed = True
        verbose_name_plural = "Taxonomies"
        db_table = 'taxonomy'


class Mealplans(models.Model):
    MealId = models.IntegerField(primary_key=True)
    MealName = models.CharField(max_length=100, default='null', null=True)
    AppId = models.CharField(max_length=100, default='null', null=True)

    class Meta:
        managed = True
        verbose_name_plural = "Mealplans"
        db_table = 'meal_plan'


class RecipeMealplans(models.Model):
    RecipeMealPlanId = models.IntegerField(primary_key=True)
    RecipeId = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="mealplan_rid")
    MealId = models.ForeignKey(Mealplans, on_delete=models.CASCADE, related_name="recipes_mealplan")
    AppId = models.CharField(max_length=100, default='null', null=True)
    UId = models.CharField(max_length=100, default='null', null=True)
    source = models.CharField(max_length=100, default='null', null=True)

    class Meta:
        managed = True
        verbose_name_plural = "RecipeMealPlans"
        db_table = 'recipe_meal_plan'











