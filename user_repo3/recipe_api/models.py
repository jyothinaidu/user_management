from django.db import models

#
# class Assets(models.Model):
#     id = models.AutoField(primary_key=True)
#     image = models.CharField(max_length=200, blank=True, null=True)
#     recipeid = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         verbose_name_plural = "Assets"
#         managed = True
#         db_table = 'assets'


class BrandRecipes(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    brand_site_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        verbose_name_plural = "BrandRecipes"
        db_table = 'brand_recipes'
        unique_together = (('recipe_id', 'brand_site_id'),)


class Classificationstext(models.Model):
    classificationstextid = models.AutoField(primary_key=True)
    classification_type_id = models.IntegerField()
    languageid = models.IntegerField()
    classification_name = models.CharField(max_length=50, blank=True, null=True)
    dtcreated = models.DateTimeField()
    createdbyuser = models.IntegerField()
    dtupdated = models.DateTimeField()
    updatedbyuser = models.IntegerField()

    class Meta:
        managed = True
        verbose_name_plural = "classificationtext"
        db_table = 'classificationstext'


class IngredientSet(models.Model):
    ingredient_set_id = models.IntegerField(primary_key=True)
    recipe_id = models.IntegerField()
    primar = models.NullBooleanField()
    display_order = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    language_id = models.IntegerField()
    country_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ingredient_set'
        verbose_name_plural = 'Ingredient Set'
        unique_together = (('ingredient_set_id', 'recipe_id'),)


class IngredientSetIngredient(models.Model):
    ingredient_set_id = models.IntegerField()
    ingredient_id = models.IntegerField()
    full_measure_unit_id = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField()
    full_measure_qty = models.CharField(max_length=50, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    language_id = models.IntegerField()
    caption = models.CharField(max_length=1000, blank=True, null=True)
    ingredient_set_ingredient_id = models.IntegerField(primary_key=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    recipeid = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ingredient_set_ingredient'
        verbose_name_plural = "Ingredient Set Ingredient"
        unique_together = (('ingredient_set_ingredient_id',
                            'language_id',
                            'country_id',
                            'ingredient_set_id',
                            'recipeid'),)


class IngredientSetNutrition(models.Model):
    ingredient_set_nutrition_id = models.AutoField(primary_key=True)
    nutritional_item_id = models.IntegerField()
    less_than = models.NullBooleanField()
    display_order = models.IntegerField(blank=True, null=True)
    ingredient_set_id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    nutrient_qty = models.CharField(max_length=50, blank=True, null=True)
    nutrition_exchange_item_id = models.IntegerField()

    class Meta:
        managed = True
        verbose_name_plural = "IngredientSetNutrition"
        db_table = 'ingredient_set_nutrition'


class IngredientSource(models.Model):
    ingredient_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name_plural = "Ingredient Source"
        db_table = 'ingredient_source'


class IngredientType(models.Model):
    ingredient_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    display_order = models.IntegerField()
    display_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name_plural = "IngredientType"
        db_table = 'ingredient_type'


class KeywordMaster(models.Model):
    keyword_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    food_type = models.CharField(max_length=1)
    language_id = models.IntegerField()
    keyword = models.CharField(max_length=60)
    kik = models.CharField(max_length=1, blank=True, null=True)
    comida = models.CharField(max_length=1, blank=True, null=True)
    canada = models.CharField(max_length=1, blank=True, null=True)
    foodserviceca = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name_plural = "KeywordMaster"
        db_table = 'keyword_master'


class KraftRecipes(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    swap_recipe = models.CharField(max_length=1)
    displayingrid = models.CharField(max_length=1)
    data_source_id = models.IntegerField()
    recipe_type_flag = models.IntegerField()
    language_id = models.IntegerField()
    entered_date = models.DateTimeField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    nbr_ingredients = models.IntegerField(blank=True, null=True)
    prep_time = models.IntegerField(blank=True, null=True)
    ready_in = models.IntegerField(blank=True, null=True)
    brand_site_id = models.IntegerField(blank=True, null=True)
    recipe_num = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    comp_recipe1 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    comp_recipe2 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    # Field renamed because it was a Python reserved word.
    yield_field = models.CharField(db_column='yield', max_length=150, blank=True, null=True)
    skill_level = models.CharField(max_length=50, blank=True, null=True)
    number_of_servings = models.CharField(max_length=150, blank=True, null=True)
    nutrition_serving_size = models.CharField(max_length=80, blank=True, null=True)
    recipe_desc = models.CharField(max_length=100, blank=True, null=True)
    recipe_name = models.CharField(max_length=100, blank=True, null=True)
    nutrition_description = models.CharField(max_length=100, blank=True, null=True)
    grid_heading_text = models.CharField(max_length=500, blank=True, null=True)
    recipe_romance_text = models.CharField(max_length=2000, blank=True, null=True)
    preparation_description = models.TextField(blank=True, null=True)
    reference_id = models.CharField(max_length=250, blank=True, null=True)
    recipe_format_id = models.IntegerField(blank=True, null=True)
    yield_volume_text = models.CharField(max_length=100, blank=True, null=True)
    nutrition_serving_text = models.CharField(max_length=100, blank=True, null=True)
    photo_reference_num = models.CharField(max_length=50, blank=True, null=True)
    approved_flag = models.IntegerField(blank=True, null=True)
    number_of_trial_servings = models.CharField(max_length=100, blank=True, null=True)
    additional_prep_time_text = models.CharField(max_length=100, blank=True, null=True)
    additional_ready_time_text = models.CharField(max_length=100, blank=True, null=True)
    aha_copy = models.CharField(max_length=100, blank=True, null=True)
    preparation_pretext = models.CharField(max_length=200, blank=True, null=True)
    grin = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        verbose_name_plural = "KraftRecipes"
        db_table = 'kraft_recipes'


class Languages(models.Model):
    language_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    language = models.CharField(max_length=100)

    class Meta:
        managed = True
        verbose_name_plural = "Languages"
        db_table = 'languages'


class RecipeIngredientAttribute(models.Model):
    recipe_ingredient_attribute_id = models.AutoField(primary_key=True)
    attribute_id = models.IntegerField()
    recipe_ingredient_id = models.IntegerField(blank=True, null=True)
    attribute_value = models.CharField(max_length=20, blank=True, null=True)
    dtcreated = models.DateTimeField(blank=True, null=True)
    createdbyuser = models.IntegerField(blank=True, null=True)
    dtupdated = models.DateTimeField(blank=True, null=True)
    updatedbyuser = models.IntegerField(blank=True, null=True)
    ingredient_set_ingredient_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        verbose_name_plural = "RecipeIngredientAttribute"
        db_table = 'recipe_ingredient_attribute'


class RecipeIngredientLinkAttribute(models.Model):
    recipe_ingredient_link_attribute_id = models.AutoField(primary_key=True)
    attribute_id = models.IntegerField()
    recipe_ingredient_link_id = models.IntegerField()
    attribute_value = models.CharField(max_length=20, blank=True, null=True)
    dtcreated = models.DateTimeField(blank=True, null=True)
    createdbyuser = models.DateTimeField(blank=True, null=True)
    dtupdated = models.DateTimeField(blank=True, null=True)
    updatedbyuser = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        verbose_name_plural = "Recipe Ingredient Link Attribute"
        db_table = 'recipe_ingredient_link_attribute'


class RecipeIngredientLinks(models.Model):
    recipe_ingredient_link_id = models.AutoField(primary_key=True)
    recipe_id = models.IntegerField()
    link_recipe_id = models.IntegerField()
    ingredient_step = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    sequence_id = models.IntegerField()
    language_id = models.IntegerField()
    recipe_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    recipe_quantity_text = models.CharField(max_length=50, blank=True, null=True)
    recipe_unit = models.CharField(max_length=50, blank=True, null=True)
    pre_preparation = models.CharField(max_length=255, blank=True, null=True)
    post_preparation = models.CharField(max_length=255, blank=True, null=True)
    full_measure_metric_qty_text = models.CharField(max_length=20, blank=True, null=True)
    metric_unit_short_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name_plural = "Recipe Ingredient Links"
        db_table = 'recipe_ingredient_links'


class RecipeIngredients(models.Model):
    recipe_ingredient_id = models.AutoField(primary_key=True)
    recipe_id = models.IntegerField()
    ingredient_step = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    ingredient_id = models.IntegerField()
    recipe_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    purchase_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    purchase_quantity_text = models.CharField(max_length=50, blank=True, null=True)
    recipe_quantity_text = models.CharField(max_length=50, blank=True, null=True)
    weights = models.CharField(max_length=50, blank=True, null=True)
    purchase_unit = models.CharField(max_length=50, blank=True, null=True)
    recipe_unit = models.CharField(max_length=75, blank=True, null=True)
    pre_preparation = models.CharField(max_length=255, blank=True, null=True)
    post_preparation = models.CharField(max_length=255, blank=True, null=True)
    recipe_metric_quantity_text = models.CharField(max_length=50, blank=True, null=True)
    recipe_metric_unit = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name_plural = "Recipe Ingredients"
        db_table = 'recipe_ingredients'


class RecipeKeywords(models.Model):
    recipe_id = models.IntegerField()
    keyword_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'recipe_keywords'
        verbose_name_plural = "Recipe Keywords"
        unique_together = (('keyword_id', 'recipe_id'),)


class RecipeNutrio(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    nutrio_recipe_id = models.IntegerField()
    language_id = models.IntegerField()

    class Meta:
        managed = True
        verbose_name_plural = "RecipeNutrio"
        db_table = 'recipe_nutrio'


class RecipeNutritionExchangeHeading(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    nutrition_exchange_item_id = models.IntegerField()
    nutrition_exchange_item_desc = models.CharField(max_length=255, blank=True, null=True)
    grid_column_heading_id = models.IntegerField(blank=True, null=True)
    grid_column_detail_id = models.IntegerField(blank=True, null=True)
    primary_ind = models.CharField(max_length=1, blank=True, null=True)
    yield_text = models.CharField(max_length=150, blank=True, null=True)
    nutrition_serving_text = models.CharField(max_length=50, blank=True, null=True)
    nutrition_reference_id = models.IntegerField(blank=True, null=True)
    nutrition_reference_unit_id = models.IntegerField(blank=True, null=True)
    nutrition_reference_text = models.CharField(max_length=20, blank=True, null=True)
    right_bite_code = models.CharField(max_length=3, blank=True, null=True)
    approved_claim_text = models.CharField(max_length=500, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    insertdate = models.DateTimeField(blank=True, null=True)
    ludate = models.DateTimeField(blank=True, null=True)
    trial_yield_text = models.CharField(max_length=100, blank=True, null=True)
    yield_volume_text = models.CharField(max_length=50, blank=True, null=True)
    trial_yield_volume_text = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_nutrition_exchange_heading'
        verbose_name_plural = "Recipe Nutrition Exchange Heading"
        unique_together = (('recipe_id', 'nutrition_exchange_item_id'),)


class RecipePhotos(models.Model):
    recipe_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)
    recipe_image_type_id = models.IntegerField(blank=True, null=True)
    sequence_char = models.CharField(max_length=10, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    recipe_photos_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    image_type = models.CharField(max_length=20, blank=True, null=True)
    mime_type = models.CharField(max_length=20, blank=True, null=True)
    image_rendition = models.CharField(max_length=15, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        verbose_name_plural = "Recipe Photos"
        db_table = 'recipe_photos'


class RecipeProducts(models.Model):
    recipe_id = models.IntegerField()
    product_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'recipe_products'
        verbose_name_plural = "Recipe Products"
        unique_together = (('product_id', 'recipe_id'),)


class RecipeTaxonomy(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    taxonomy_id = models.IntegerField()
    insert_date = models.DateTimeField()
    ludate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_taxonomy'
        verbose_name_plural = "Recipe Taxonomy"
        unique_together = (('recipe_id', 'taxonomy_id'),)


class RecipeTips(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    tip_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    sequence_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'recipe_tips'
        verbose_name_plural = "Recipe Tips"
        unique_together = (('recipe_id', 'tip_id'),)


class Taxonomy(models.Model):
    taxonomy_type_id = models.IntegerField(blank=True, null=True)
    taxonomy_id = models.IntegerField(primary_key=True)
    taxonomy_name = models.CharField(max_length=200)
    parent_taxonomy_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField()
    country_id = models.IntegerField()
    insert_date = models.DateTimeField(blank=True, null=True)
    ludate = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    hierarchy_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'taxonomy'
        verbose_name_plural = "Taxonomy"
        unique_together = (('taxonomy_id', 'country_id', 'language_id'),)


class TaxonomyType(models.Model):
    taxonomy_type_id = models.IntegerField(primary_key=True)
    taxonomy_type_name = models.CharField(max_length=100)
    insert_date = models.DateTimeField(blank=True, null=True)
    ludate = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1)

    class Meta:
        managed = True
        verbose_name_plural = "Taxonomy Type"
        db_table = 'taxonomy_type'


class TaxonomyTypeResource(models.Model):
    taxonomy_type_id = models.IntegerField(primary_key=True)
    taxonomy_type_name = models.CharField(max_length=100)
    created_by_user_id = models.IntegerField(blank=True, null=True)
    updated_by_user_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    resource_id = models.IntegerField(blank=True, null=True)
    is_active = models.NullBooleanField()

    class Meta:
        managed = True
        verbose_name_plural = "Taxonomy Type resource"
        db_table = 'taxonomy_type_resource'


class RecipeClassifications(models.Model):
    recipe_id = models.IntegerField(null=False)
    classification_type_id = models.IntegerField(null=False)
    status = models.CharField(default='A', null=False, max_length=2)
    insertdate = models.DateTimeField(auto_now_add=True)
    ludate = models.DateTimeField()
    classification_category_id = models.IntegerField(null=False)

    class Meta:
        managed = True
        verbose_name_plural = "Recipe Classifications"
        db_table = 'recipe_classifications'

