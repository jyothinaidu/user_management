from django.db import models
from django.contrib.postgres.fields import ArrayField

import uuid

from datetime import datetime


"""
Recipes one to many fields, tables
"""


class Recipes(models.Model):
    """
    Recipes Model:
                    AdServingKeywords,
                    --AlternateLanguageRecipes,
                    --Assets,
                    AverageRating,
                    BrandId,
                    Branding,
                    CSSSkins,
                    CarbCounter,
                    --Categories,
                    --Classifications,
                    ComplimentaryRecipes,
                    --CookingMethod,
                    Copyright,
                    --Courses,
                    DietExchange,
                    --DishDetails,
                    EndDate,
                    HasVideo,
                    --Ingredients,
                    IsHealthyLiving,
                    KRLId,
                    --KeyIngredients,
                    Keywords,
                    LanguageId,
                    --LifeStyles,
                    NumberOfIngredients,
                    NumberOfRatings,
                    NumberOfRatingsWithComments,
                    NumberOfServings,
                    NumberOfTrialServings,
                    NutritionBonus,
                    NutritionExchangeItemId,
                    NutritionGridItems,
                    --NutritionItems,
                    NutritionServingText,
                    PrepStepImage,
                    PreparationDescription,
                    PreparationPreText,
                    --PreparationSteps,
                    PreparationTime,
                    --Promotion,
                    --Ratings,
                    RecipeDisplayFormatId,
                    RecipeId,
                    RecipeName,
                    RecipeType,
                    --RelatedData,
                    --RiseIngredients,
                    --RiseTaxonomy,
                    --Riserecipe,
                    RomanceText,
                    --Tips,
                    TotalTime,
                    TradeMarkInfo,
                    --Video,
                    Yield,
    """

    # pid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    pid = models.AutoField(primary_key=True)
    AdServingKeywords = models.CharField(max_length=100, null=True, default='null')
    # AlternateLanguageRecipes = models.CharField(max_length=100, null=True, default='null')
    AverageRating = models.CharField(max_length=100, null=True, default='null')
    BrandId = models.IntegerField(default=0)
    Branding = models.CharField(max_length=100, null=True, default='null')
    CSSSkins = models.CharField(max_length=100, null=True, default='null')
    CarbCounter = models.CharField(max_length=50, null=True, default='null')
    # Classifications = ArrayField(models.CharField(max_length=50, null=True, default='null'))
    ComplimentaryRecipes = models.CharField(max_length=50, null=True, default='null')
    Copyright = models.CharField(max_length=50, null=True, default='null')
    DietExchange = models.CharField(max_length=50, null=True, default='null')
    EndDate = models.DateField(blank=True)
    HasVideo = models.BooleanField(default=False)
    IsHealthyLiving = models.BooleanField(default=False)
    KRLId = models.CharField(max_length=50, null=True, default='null')
    Keywords = models.CharField(max_length=50, null=True, default='null')
    LanguageId = models.IntegerField(default=1)
    NumberOfIngredients = models.IntegerField(default=0)
    NumberOfRatings = models.IntegerField(default=0)
    NumberOfRatingsWithComments = models.IntegerField(default=0)
    NumberOfServings = models.IntegerField(default=0)
    NumberOfTrialServings = models.CharField(max_length=30, null=True, default='null')
    NutritionBonus = models.CharField(max_length=30, null=True, default='null')
    NutritionExchangeItemId = models.IntegerField(default=0)
    NutritionGridItems = models.CharField(max_length=30, null=True, default='null')
    NutritionServingText = models.CharField(max_length=30, null=True, default='null')
    PrepStepImage = models.CharField(max_length=30, null=True, default='null')
    PreparationDescription = models.TextField(default="null")
    PreparationPreText = models.CharField(max_length=30, null=True, default='null')
    PreparationTime = models.IntegerField(default=0)
    RecipeDisplayFormatId = models.IntegerField(default=0)
    RecipeId = models.CharField(max_length=30, null=True, default='null')
    RecipeName = models.CharField(max_length=30, null=True, default='null')
    RecipeType = models.IntegerField(default=0)
    RomanceText = models.TextField(default="null")
    SEOName = models.CharField(max_length=30, null=True, default='null')
    TotalTime = models.IntegerField(default=0)
    TradeMarkInfo = models.CharField(max_length=30, null=True, default='null')
    Yield = models.CharField(max_length=30, null=True, default='null')
    # owner = models.ForeignKey(
    #     'auth.User',
    #     related_name='recipes',
    #     on_delete=models.CASCADE)

    class Meta:
        managed = True
        verbose_name_plural = "Recipes"
        db_table = "recipes"


"""
assets one to many pictureformats
"""


class Assets(models.Model):
    """
    Assets Model:
                    pictureformats,
                    aspectRatio,
                    assetDescription,
                    author,
                    id,
                    imageType,
                    length,
                    mimeType,
                    playerId,
                    publicationDate,
                    sequence,
                    sourceName,
                    status,
                    title,
                    type,
                    videoID,
                    null value in column "recipes_assets_id" violates not-null constraint
DETAIL:  Failing row contains (1, 123x21, fff, author1, 12, 12, 12, mime1, 2,
 2018-06-07, 1, Y, Title1, newtype, 2, null).
    """
    # pid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    pid = models.AutoField(primary_key=True)
    recipes_assets = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="recipeassets")
    aspectRatio = models.CharField(max_length=30, null=True, default='null')
    assetDescription = models.TextField(default='null')
    author = models.CharField(max_length=20, null=True, default='null')
    id = models.IntegerField(default=0, null=True)
    imageType = models.CharField(max_length=20, null=True, default='null')
    length = models.CharField(max_length=20, null=True, default='null')
    mimeType = models.CharField(max_length=20, null=True, default='null')
    playerId = models.CharField(max_length=20, null=True, default='null')
    publicationDate = models.DateField(default=datetime.now, blank=True)
    sequence = models.CharField(max_length=20, null=True, default='null')
    status = models.CharField(max_length=20, null=True, default='null')
    title = models.CharField(max_length=20, null=True, default='null')
    type = models.CharField(max_length=20, null=True, default='null')
    videoID = models.CharField(max_length=20, null=True, default='null')

    class Meta:
        managed = True
        verbose_name_plural = "Assets"
        db_table = 'assets'

    def __str__(self):
        return f'{self.pid}'


# class CookingMethod(models.Model):
#     id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
#     Name = models.CharField(max_length=20, null=True, default='null')


class PictureFormats(models.Model):
    # id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    id = models.AutoField(primary_key=True)
    assets = models.ForeignKey(Assets, on_delete=models.CASCADE, related_name='pictureformats')

    rendition = models.CharField(max_length=20, null=True, default='null')
    url = models.CharField(max_length=200, null=True, default='null')

    class Meta:
        managed = True
        verbose_name_plural = "PictureFormats"
        db_table = 'pictureformats'


class AlternateLanguages(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    LanguageId = models.CharField(max_length=20, default='null', null=True)
    RecipeId = models.CharField(max_length=20, default='null', null=True)
    SiteId = models.CharField(max_length=20, default='null', null=True)
    recipes_alternate_language = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='alternatelanguages')

    class Meta:
        managed = True
        verbose_name_plural = "AlternateLanguages"
        db_table = 'alternatelanguages'


class Category(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    CategoryId = models.IntegerField(default=0)
    CategoryName = models.CharField(max_length=20, default='null', null=True)
    CategoryRank = models.IntegerField(default=1)
    SubCategoryId = models.IntegerField(default=0)
    SubCategoryName = models.CharField(max_length=20, default='null', null=True)
    SubCategoryRank = models.IntegerField(default=1)
    recipes_categories = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="categories")

    class Meta:
        managed = True
        verbose_name_plural = "categories"
        db_table = "categories"
