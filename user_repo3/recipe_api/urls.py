from django.urls import path, include
from django.conf.urls import url
from .views import *
from rest_framework import routers
from .views1 import AssetsView, RecipesView, PicturesView
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Recipes API')

router = routers.DefaultRouter()
router.register('assets', AssetsView)
router.register('branchrecipes', BranchRecipesView)
router.register('classificationtext', ClassificationsTextView)
router.register('ingredientset', IngredientSetView)
router.register('ingredientsetingredient', IngredientSetIngredientView)
router.register('ingredientsetnutrition', IngredientSetNutritionView)
router.register('ingredientsource', IngredientSourceView)
router.register('ingredienttype', IngredientTypeView)
router.register('keywordmaster', KeywordMasterView)
router.register('kraftrecipes', KraftRecipesView)
router.register('languages', LanguagesView)
router.register('recipeingredientsattribute', RecipeIngredientAttributeView)
router.register('recipeingredientlinkattribute', RecipeIngredientLinkAttributeView)
router.register('recipeingredients', RecipeIngredientsView)
router.register('recipekeywords', RecipeKeywordsView)
router.register('recipenutrio', RecipeNutrioView)
router.register('recipenutritionexchangeheading', RecipeNutritionExchangeHeadingView)
router.register('recipephotos', RecipePhotosView)
router.register('recipeproducts', RecipeProductsView)
router.register('recipetaxonomy', RecipeTaxonomyView)
router.register('recipetips', RecipeTipsView)
router.register('taxonomy', TaxonomyView)
router.register('taxonomytype', TaxonomyTypeView)
router.register('taxonomytyperesource', TaxonomyTypeResourceView)
router.register('pictureformats', PicturesView)
router.register('v0.1', RecipesView)

urlpatterns = [
    path('', include(router.urls)),
    # url(r'^register/$', views.RegistrationView.as_view()),
    path(r'swagger-docs/', schema_view),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('recipesapi/', RecipesView.as_view())
    # url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
