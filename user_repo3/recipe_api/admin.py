from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('recipe_api')

for model_name, model in app.models.items():
    admin.site.register(model)

# from django.apps import apps, AppConfig
#
# # Register your models here.
#
#
# class CustomApp(AppConfig):
#     name = 'recipe_api'
#
#     def ready(self):
#         models = apps.get_models()
#         for model in models:
#             try:
#                 admin.site.register(model)
#             except admin.sites.AlreadyRegistered:
#                 pass
