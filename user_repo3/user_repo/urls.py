from django.conf.urls import url, include
# from rest_framework import routers
from user_management import views
from user_management.user_management_api import *
# from user_management.user_management_api import FirebaseAuthentication
from user_management import user_management_api
# router = routers.DefaultRouter()
# router.register(r'users', views.UsersViewSet)
# router.register(r'applications', views.ApplicationViewSet)
# router.register(r'profileattributes', views.ProfileAttributesViewSet)
# router.register(r'profile', views.ProfileViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsabuserle API.
from django.contrib.auth.views import LogoutView, LoginView
# from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from user_management.views import LoginView,LogoutView,TestAuthView,AdminLoginView,AdminLogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView,TokenObtainSlidingView,
    TokenRefreshSlidingView
)
from user_management import views
from recipes_sample import views as recipesviews

from datetime import timedelta

from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_swagger_view(title='Kraft API')

urlpatterns = [



    url(r'^$', user_management_api.login, name='admin_firebase_auth'),
    url(r'^admin/v0/', admin.site.urls),
    url(r'^swagger/v0/$', schema_view,name="swagger-details"),
    url(r'^api/dashboard/$', user_management_api.api_root),
    url(r'^api-auth/v0/', include('rest_framework.urls')),
    url(r'^user/login/v0/', obtain_jwt_token, name='api-token-auth'),

    url(r'^user/v0/$', views.UsersListView.as_view(), name="users_list"),
    url(r'^user/auth/login/v0/$', views.UserLoginAPIView.as_view(), name='admin_firebase_auth'),
    url(r'^user/auth/logout/v0/$', AdminLogoutView.as_view(), name='admin_firebase_logout'),
    url(r'^user/auth/create-user/v0/$', views.UserRegistrationAPIView.as_view(), name="user_create"),
    url(r'^user/auth/delete-user/v0/$', views.UserDeleteView.as_view(), name="user_delete"),


    url(r'^verify/(?P<verification_key>.+)/$',views.UserEmailVerificationAPIView.as_view(),name='email_verify'),

    # url(r'^user/preferences/v0/$', views.PreferencesListView.as_view(), name="preferences_list"),
    url(r'^user/preferences/create/v0/$', views.UserPreferenceAPIView.as_view(), name="preferences_create"),
    url(r'^user/answers/create/v0/$', views.UserAnswersCreateView.as_view(), name="answers_create"),
    url(r'^user/preferences/favourite/create/v0/$', views.PreferencesFavouriteCreateView.as_view(), name="favourites_create"),
    # url(r'^user/preferences/favourite/v0/$', views.PreferencesFavouriteListApiView.as_view(), name="favourites_list"),


    # url(r'^$', views.UsersListView.as_view(), name="users_list"),


    # url(r'^user/list/$', views.UsersListView.as_view(), name="users_list"),



    # url(r'^v0/user/(?P<pk>\d+)/$', views.UserDetailView.as_view(), name="user_detail"),
    # url(r'^v0/user/(?P<pk>\d+)/detail/$', views.UserDetailView.as_view(), name="user_detail"),
    # url(r'^v0/user/(?P<pk>\d+)/update/$', views.UserUpdateView.as_view(), name="user_update"),


    # url(r'^user/(?P<pk>\d+)/delete/$', views.UserDeleteView.as_view(), name="user_delete"),






    url(r'^assets/$',recipesviews.AssetsView.as_view(),name=recipesviews.AssetsView.name),
    url(r'^assets/(?P<pk>[0-9]+)$',recipesviews.AssetsDetailView.as_view(),name=recipesviews.AssetsDetailView.name),
    url(r'^categories/$',recipesviews.CategoryView.as_view(),name=recipesviews.CategoryView.name),
    url(r'^categories/(?P<pk>[0-9]+)$',recipesviews.CategoryDetailView.as_view(),name=recipesviews.CategoryDetailView.name),
    url(r'^dishes/$',recipesviews.DishView.as_view(),name=recipesviews.DishView.name),
    url(r'^dishes/(?P<pk>[0-9]+)$',recipesviews.DishDetailView.as_view(),name=recipesviews.DishDetailView.name),
    url(r'^ingredients/$',recipesviews.IngredientView.as_view(),name=recipesviews.IngredientView.name),
    url(r'^ingredients/(?P<pk>[0-9]+)$',recipesviews.IngredientDetailView.as_view(),name=recipesviews.IngredientDetailView.name),
    url(r'^riseingredients/$',recipesviews.RiseIngredientView.as_view(),name=recipesviews.RiseIngredientView.name),
    url(r'^riseingredients/(?P<pk>[0-9]+)$',recipesviews.RiseIngredientDetailView.as_view(),name=recipesviews.RiseIngredientDetailView.name),
    url(r'^taxonomy/$',recipesviews.TaxonomyView.as_view(),name=recipesviews.TaxonomyView.name),
    url(r'^taxonomy/(?P<pk>[0-9]+)$',recipesviews.TaxonomyDetailView.as_view(),name=recipesviews.TaxonomyDetailView.name),
    url(r'^mealplanrecipes/$',recipesviews.RecipeMealPlanView.as_view(),name=recipesviews.RecipeMealPlanView.name),
    url(r'^mealplanrecipes/(?P<pk>[0-9]+)$',recipesviews.RecipeMealPlanDetailView.as_view(),name=recipesviews.RecipeMealPlanDetailView.name),
    url(r'^mealplans/$',recipesviews.MealplanView.as_view(),name=recipesviews.MealplanView.name),
    url(r'^mealplan/(?P<pk>[0-9]+)$',recipesviews.MealplanDetailView.as_view(),name=recipesviews.MealplanDetailView.name),
    url(r'^recipes/$',recipesviews.RecipesView.as_view(),name=recipesviews.RecipesView.name),
    url(r'^recipes/(?P<pk>[0-9]+)$',recipesviews.RecipesDetailView.as_view(),name=recipesviews.RecipesDetailView.name),
    # url(r'^swagger/$', schema_view,name="swagger-details"),
























]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

              # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}