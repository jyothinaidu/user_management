from rest_framework import serializers
from .modes1 import Assets, PictureFormats, Recipes, AlternateLanguages, Category
# from django.contrib.auth.models import User


class PictureFormatSerializer(serializers.ModelSerializer):

    class Meta:
        model = PictureFormats
        # fields = ('rendition', 'url')
        fields = '__all__'


class AssetsSerialzer(serializers.ModelSerializer):
    pictureformats = PictureFormatSerializer(many=True)

    class Meta:
        model = Assets
        fields = (
            'pictureformats',
            'aspectRatio',
            'assetDescription',
            'author',
            'id',
            'imageType',
            'length',
            'mimeType',
            'playerId',
            'publicationDate',
            'sequence',
            'status',
            'title',
            'type',
            'videoID',
        )

    def create(self, validated_data):
        picture_format_data = validated_data.pop('pictureformats')
        # print('picture_format')
        assets = Assets.objects.create(**validated_data)
        for pictureformat in picture_format_data:
            PictureFormats.objects.create(assets=assets, **pictureformat)
        return assets


class AlternateLanguagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlternateLanguages
        fields = ('LanguageId', 'RecipeId', 'SiteId')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('CategoryId', 'CategoryName', 'CategoryRank', 'SubCategoryId', 'SubCategoryName',
                  'SubCategoryRank')


class RecipesSerializer(serializers.ModelSerializer):

    Assets = AssetsSerialzer(many=True)
    AlternateLanguageRecipes = AlternateLanguagesSerializer(many=True)
    Categories = CategorySerializer(many=True)
    Classifications = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        model = Recipes
        fields = (
            'AdServingKeywords',
            'AlternateLanguageRecipes',
            'Assets',
            'AverageRating',
            'BrandId',
            'Branding',
            'CSSSkins',
            'CarbCounter',
            'Categories',
            'Classifications',
            'ComplimentaryRecipes',
            # --CookingMethod,
            'Copyright',
            # --Courses,
            'DietExchange',
            # --DishDetails,
            'EndDate',
            'HasVideo',
            # --Ingredients,
            'IsHealthyLiving',
            'KRLId',
            # --KeyIngredients,
            'Keywords',
            'LanguageId',
            # --LifeStyles,
            'NumberOfIngredients',
            'NumberOfRatings',
            'NumberOfRatingsWithComments',
            'NumberOfServings',
            'NumberOfTrialServings',
            'NutritionBonus',
            'NutritionExchangeItemId',
            'NutritionGridItems',
            # 'NutritionItems',
            'NutritionServingText',
            'PrepStepImage',
            'PreparationDescription',
            'PreparationPreText',
            # --PreparationSteps,
            'PreparationTime',
            # --Promotion,
            # --Ratings,
            'RecipeDisplayFormatId',
            'RecipeId',
            'RecipeName',
            'RecipeType',
            # --RelatedData,
            # --RiseIngredients,
            # --RiseTaxonomy,
            # --Riserecipe,
            'RomanceText',
            # --Tips,
            'TotalTime',
            'TradeMarkInfo',
            # --Video,
            'Yield',
        )

    def create(self, validated_data):
        recipe_asset_data = validated_data.pop('recipeassets')
        alternate_language_data = validated_data.pop('alternatelanguages')
        category_data = validated_data.pop('categories')
        recipes = Recipes.objects.create(**validated_data)
        alternatelanguages = Recipes.objects.create(**validated_data)
        categories = Recipes.objects.create(**validated_data)
        for recipe_asset in recipe_asset_data:
            Assets.objects.create(recipes=recipes, **recipe_asset)
        for alternate_language in alternate_language_data:
            AlternateLanguages.objects.create(alternatelanguages=alternatelanguages, **alternate_language)
        for category in category_data:
            Category.objects.create(categories=categories, **category)
        return recipes
