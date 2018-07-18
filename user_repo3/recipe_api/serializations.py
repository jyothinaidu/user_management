# from rest_framework import serializers
# from .models import *
#
#
# class AssetsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assets
#         fields = '__all__'
#
#
# class BranchRecipesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BrandRecipes
#         fields = '__all__'
#
#
# class ClassificationstextSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Classificationstext
#         fields = '__all__'
#
#
# class IngredientSetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IngredientSet
#         fields = '__all__'
#
#
# class IngredientSetIngredientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IngredientSetIngredient
#         fields = '__all__'
#
#
# class IngredientSetNutritionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IngredientSetNutrition
#         fields = '__all__'
#
#
# class IngredientSourceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IngredientSource
#         fields = '__all__'
#
#
# class IngredientTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IngredientType
#         fields = '__all__'
#
#
# class KeywordMasterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = KeywordMaster
#         fields = '__all__'
#
#
# class KraftRecipesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = KraftRecipes
#         fields = '__all__'
#
#
# class LanguagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Languages
#         fields = '__all__'
#
#
# class RecipeIngredientAttributeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeIngredientAttribute
#         fields = '__all__'
#
#
# class RecipeIngredientLinkAttributeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeIngredientAttribute
#         fields = '__all__'
#
#
# class RecipeIngredientLinksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeIngredientAttribute
#         fields = '__all__'
#
#
# class RecipeIngredientsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeIngredients
#         fields = '__all__'
#
#
# class RecipeKeywordsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeKeywords
#         fields = '__all__'
#
#
# class RecipeNutrioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeKeywords
#         fields = '__all__'
#
#
# class RecipeNutritionExchangeHeadingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeNutritionExchangeHeading
#         fields = '__all__'
#
#
# class RecipePhotosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipePhotos
#         fields = '__all__'
#
#
# class RecipeProductsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeProducts
#         fields = '__all__'
#
#
# class RecipeTaxonomySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeProducts
#         fields = '__all__'
#
#
# class RecipeTipsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeTips
#         fields = '__all__'
#
#
# class TaxonomySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeTips
#         fields = '__all__'
#
#
# class TaxonomyTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TaxonomyType
#         fields = '__all__'
#
#
# class TaxonomyTypeResourceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TaxonomyTypeResource
#         fields = '__all__'
#
#
# class RecipesSerializer(serializers.Serializer):
#     Assets = AssetsSerializer()
#     BranchRecipes = BranchRecipesSerializer()
#     Classificationstext = ClassificationstextSerializer()
#     IngredientSet = IngredientSetSerializer()
#     IngredientSetIngredient = IngredientSetIngredientSerializer()
#     IngredientSetNutrition = IngredientSetNutritionSerializer()
#     IngredientSource = IngredientSourceSerializer()
#     IngredientType = IngredientTypeSerializer()
#     KeywordMaster = KeywordMasterSerializer()
#     KraftRecipes = KraftRecipesSerializer()
#     languages = LanguagesSerializer()
#     RecipeIngredientAttribute = RecipeIngredientAttributeSerializer()
#     RecipeIngredientLinkAttribute = RecipeIngredientLinkAttributeSerializer()
#     RecipeIngredientLinks = RecipeIngredientLinksSerializer()
#     RecipeIngredients = RecipeIngredientsSerializer()
#     RecipeKeywords = RecipeKeywordsSerializer()
#
