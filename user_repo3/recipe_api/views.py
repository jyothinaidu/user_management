from rest_framework import viewsets, views
from .models import *
from .serializers import *
# from .serializations import RecipesSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


# class AssetsView(viewsets.ModelViewSet):
#     queryset = Assets.objects.all()
#     serializer_class = AssetsSerializer


class BranchRecipesView(viewsets.ModelViewSet):
    queryset = BrandRecipes.objects.all()
    serializer_class = BranchRecipesSerializer


class ClassificationsTextView(viewsets.ModelViewSet):
    queryset = Classificationstext.objects.all()
    serializer_class = ClassificationstextSerializer


class IngredientSetView(viewsets.ModelViewSet):
    queryset = IngredientSet.objects.all()
    serializer_class = IngredientSetSerializer


class IngredientSetIngredientView(viewsets.ModelViewSet):
    queryset = IngredientSetIngredient.objects.all()
    serializer_class = IngredientSetIngredientSerializer


class IngredientSetNutritionView(viewsets.ModelViewSet):
    queryset = IngredientSetNutrition.objects.all()
    serializer_class = IngredientSetNutritionSerializer


class IngredientSourceView(viewsets.ModelViewSet):
    queryset = IngredientSource.objects.all()
    serializer_class = IngredientSourceSerializer


class IngredientTypeView(viewsets.ModelViewSet):
    queryset = IngredientType.objects.all()
    serializer_class = IngredientTypeSerializer


class KeywordMasterView(viewsets.ModelViewSet):
    queryset = KeywordMaster.objects.all()
    serializer_class = KeywordMasterSerializer


class KraftRecipesView(viewsets.ModelViewSet):
    queryset = KraftRecipes.objects.all()
    serializer_class = KraftRecipesSerializer


class LanguagesView(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer


class RecipeIngredientAttributeView(viewsets.ModelViewSet):
    queryset = RecipeIngredientAttribute.objects.all()
    serializer_class = RecipeIngredientAttributeSerializer


class RecipeIngredientLinkAttributeView(viewsets.ModelViewSet):
    queryset = RecipeIngredientLinkAttribute.objects.all()
    serializer_class = RecipeIngredientLinkAttributeSerializer


class RecipeIngredientLinksView(viewsets.ModelViewSet):
    queryset = RecipeIngredientLinks.objects.all()
    serializer_class = RecipeIngredientLinksSerializer


class RecipeIngredientsView(viewsets.ModelViewSet):
    queryset = RecipeIngredients.objects.all()
    serializer_class = RecipeIngredientsSerializer


class RecipeKeywordsView(viewsets.ModelViewSet):
    queryset = RecipeKeywords.objects.all()
    serializer_class = RecipeKeywordsSerializer


class RecipeNutrioView(viewsets.ModelViewSet):
    queryset = RecipeNutrio.objects.all()
    serializer_class = RecipeNutrioSerializer


class RecipeNutritionExchangeHeadingView(viewsets.ModelViewSet):
    queryset = RecipeNutritionExchangeHeading.objects.all()
    serializer_class = RecipeNutritionExchangeHeadingSerializer


class RecipePhotosView(viewsets.ModelViewSet):
    queryset = RecipePhotos.objects.all()
    serializer_class = RecipePhotosSerializer


class RecipeProductsView(viewsets.ModelViewSet):
    queryset = RecipeProducts.objects.all()
    serializer_class = RecipeProductsSerializer


class RecipeTaxonomyView(viewsets.ModelViewSet):
    queryset = RecipeTaxonomy.objects.all()
    serializer_class = RecipeTaxonomySerializer


class RecipeTipsView(viewsets.ModelViewSet):
    queryset = RecipeTips.objects.all()
    serializer_class = RecipeTipsSerializer


class TaxonomyView(viewsets.ModelViewSet):
    queryset = Taxonomy.objects.all()
    serializer_class = TaxonomySerializer


class TaxonomyTypeView(viewsets.ModelViewSet):
    queryset = TaxonomyType.objects.all()
    serializer_class = TaxonomyTypeSerializer


class TaxonomyTypeResourceView(viewsets.ModelViewSet):
    queryset = TaxonomyTypeResource.objects.all()
    serializer_class = TaxonomyTypeResourceSerializer


# class RecipesView(views.APIView):
#
#     def get(self, request):
#         recipedata = JSONRenderer().render(RecipesSerializer.data)
#         return Response(recipedata, content_type='application/json')


