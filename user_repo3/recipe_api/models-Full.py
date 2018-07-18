# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brands(models.Model):
    brand_site_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    classic_brand = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    brand_name = models.CharField(max_length=50)
    referrer = models.CharField(max_length=50)
    url = models.CharField(max_length=60)
    video_sponsor = models.BooleanField()
    logo_image = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brands'


class BrandSiteTipCategory(models.Model):
    brand_site_tip_category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brand_site_tip_category'


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    country = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'countries'


class Languages(models.Model):
    language_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    language = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'languages'


class BrandSiteTip(models.Model):
    brand_site_tip_id = models.AutoField(primary_key=True)
    brand_site = models.ForeignKey('Brands', models.DO_NOTHING)
    language = models.ForeignKey('Languages', models.DO_NOTHING)
    text = models.CharField(max_length=800)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()
    brand_site_tip_category = models.ForeignKey('BrandSiteTipCategory', models.DO_NOTHING)
    active_flag = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'brand_site_tip'


class Rsubcategories(models.Model):
    rcategory_id = models.IntegerField(primary_key=True)
    rsubcategory_id = models.AutoField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    menu_planner = models.CharField(max_length=1)
    subcat_rank = models.IntegerField(blank=True, null=True)
    rsubcategory = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rsubcategories'
        unique_together = (('rcategory_id', 'rsubcategory_id'),)


class KeywordMaster(models.Model):
    keyword_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    food_type = models.CharField(max_length=1)
    language = models.ForeignKey('Languages', models.DO_NOTHING)
    keyword = models.CharField(max_length=60)
    kik = models.CharField(max_length=1, blank=True, null=True)
    comida = models.CharField(max_length=1, blank=True, null=True)
    canada = models.CharField(max_length=1, blank=True, null=True)
    foodserviceca = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'keyword_master'


class CategoryGroupType(models.Model):
    category_group_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    descr = models.CharField(max_length=250)
    status = models.IntegerField()
    dtcreated = models.DateTimeField()
    createdbyuser = models.IntegerField()
    dtupdated = models.DateTimeField()
    updatedbyuser = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'category_group_type'


class CategoryGroups(models.Model):
    category_group_id = models.AutoField(primary_key=True)
    brand_site = models.ForeignKey(Brands, models.DO_NOTHING)
    language = models.ForeignKey('Languages', models.DO_NOTHING)
    category_group_name = models.CharField(max_length=50)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    rank = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    category_group_type = models.ForeignKey(CategoryGroupType, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'category_groups'


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
    yield_field = models.CharField(db_column='yield', max_length=150, blank=True, null=True)
    # Field renamed because it was a Python reserved word.
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
        db_table = 'kraft_recipes'


class ProductCategories(models.Model):
    product_category_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    product_category_description = models.CharField(max_length=50)
    product_category_image_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'product_categories'


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    product_location = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    product_category = models.ForeignKey(ProductCategories, models.DO_NOTHING)
    brand_site = models.ForeignKey(Brands, models.DO_NOTHING, blank=True, null=True)
    hyper_link = models.CharField(max_length=100, blank=True, null=True)
    product_title = models.CharField(max_length=120, blank=True, null=True)
    product_description = models.CharField(max_length=7500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'products'


class ShoppingAisles(models.Model):
    aisle_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    language = models.ForeignKey(Languages, models.DO_NOTHING)
    aisle_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'shopping_aisles'


class IngredientTypeOld(models.Model):
    ingredient_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    ludate = models.DateTimeField(blank=True, null=True)
    insertdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredient_type_old'


class IngredientSource(models.Model):
    ingredient_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredient_source'


class NlBrandCategories(models.Model):
    nl_brand_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    nl_category = models.ForeignKey('NlCategoryLookups', models.DO_NOTHING)
    nl_brand_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'nl_brand_categories'


class Tips(models.Model):
    tip_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    language = models.ForeignKey(Languages, models.DO_NOTHING, blank=True, null=True)
    brand_site = models.ForeignKey(Brands, models.DO_NOTHING, blank=True, null=True)
    tip_name = models.CharField(max_length=100)
    search_word = models.CharField(max_length=100, blank=True, null=True)
    tip_description = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tips'


class RiaLoadHistory(models.Model):
    load_id = models.IntegerField(primary_key=True)
    load_start = models.DateTimeField()
    record_count = models.DecimalField(max_digits=9, decimal_places=0)
    target_table = models.CharField(max_length=50)
    load_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ria_load_history'


class Seasons(models.Model):
    season_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    season = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'seasons'		


class SpecialOccasions(models.Model):
    special_occasion_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    holiday_indicator = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    effective_date = models.DateTimeField()
    termination_date = models.DateTimeField()
    special_occasion_name = models.CharField(max_length=60)
    language = models.ForeignKey(Languages, models.DO_NOTHING, blank=True, null=True)
    season = models.ForeignKey(Seasons, models.DO_NOTHING, blank=True, null=True)
    brand_site_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'special_occasions'


class TaxonomyType(models.Model):
    taxonomy_type_id = models.IntegerField(primary_key=True)
    taxonomy_type_name = models.CharField(max_length=100)
    insert_date = models.DateTimeField(blank=True, null=True)
    ludate = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'taxonomy_type'


class Tcategories(models.Model):
    tcategory_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    language = models.ForeignKey(Languages, models.DO_NOTHING, blank=True, null=True)
    tcategory_type = models.CharField(max_length=50)
    tcategory_description = models.CharField(max_length=50)
    tcategory_image_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tcategories'


class Tsubcategories(models.Model):
    tcategory = models.ForeignKey(Tcategories, models.DO_NOTHING, primary_key=True)
    tsubcategory_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    tsubcategory_description = models.CharField(max_length=50, blank=True, null=True)
    tsubcategory_image_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tsubcategories'
        unique_together = (('tcategory', 'tsubcategory_id'),)


class Assets(models.Model):
    image = models.CharField(max_length=200, blank=True, null=True)
    recipeid = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'assets'


class Attribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    attribute_name = models.CharField(max_length=50)
    status = models.CharField(max_length=1, blank=True, null=True)
    dtcreated = models.DateTimeField(blank=True, null=True)
    createdbyuser = models.IntegerField(blank=True, null=True)
    dtupdated = models.DateTimeField(blank=True, null=True)
    updatedbyuser = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'attribute'


class Autonomykeywordexport(models.Model):
    contentid = models.BigIntegerField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'autonomykeywordexport'


class Azureblobimagearchive(models.Model):
    imageid = models.AutoField()
    imagename = models.CharField(max_length=200, blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    isarchived = models.NullBooleanField()
    isdeleted = models.NullBooleanField()
    deleteddt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'azureblobimagearchive'


class Azureblobimages(models.Model):
    imageid = models.AutoField()
    imageurl = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'azureblobimages'


class AzurerecipePhotos(models.Model):
    recipe_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)
    recipe_image_type_id = models.IntegerField(blank=True, null=True)
    sequence_char = models.CharField(max_length=10, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    recipe_photos_id = models.AutoField()
    author = models.CharField(max_length=30, blank=True, null=True)
    image_type = models.CharField(max_length=20, blank=True, null=True)
    mime_type = models.CharField(max_length=20, blank=True, null=True)
    image_rendition = models.CharField(max_length=15, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'azurerecipe_photos'


class AzurerecipePhotos1(models.Model):
    recipe_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)
    recipe_image_type_id = models.IntegerField(blank=True, null=True)
    sequence_char = models.CharField(max_length=10, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    recipe_photos_id = models.AutoField()
    author = models.CharField(max_length=30, blank=True, null=True)
    image_type = models.CharField(max_length=20, blank=True, null=True)
    mime_type = models.CharField(max_length=20, blank=True, null=True)
    image_rendition = models.CharField(max_length=15, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'azurerecipe_photos1'


class BannerType(models.Model):
    banner_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    status = models.IntegerField()
    dtcreated = models.DateTimeField()
    createdbyuser = models.IntegerField()
    dtupdated = models.DateTimeField()
    updatedbyuser = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'banner_type'


class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    banner_type = models.ForeignKey('BannerType', models.DO_NOTHING)
    language_id = models.IntegerField()
    description = models.CharField(max_length=100)
    use_custom_banner = models.BooleanField()
    status = models.IntegerField()
    dtcreated = models.DateTimeField()
    createdbyuser = models.IntegerField()
    dtupdated = models.DateTimeField()
    updatedbyuser = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'banner'


class BrandKeywords(models.Model):
    brand_site = models.ForeignKey('Brands', models.DO_NOTHING)
    keyword = models.ForeignKey('KeywordMaster', models.DO_NOTHING, primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    translation = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brand_keywords'
        unique_together = (('keyword', 'brand_site'),)


class BrandRecipecategories(models.Model):
    rcategory_id = models.IntegerField(primary_key=True)
    brand_site = models.ForeignKey('Brands', models.DO_NOTHING)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    translation = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brand_recipecategories'
        unique_together = (('rcategory_id', 'brand_site'),)


class BrandRecipecatsubcategories(models.Model):
    brand_site = models.ForeignKey('Brands', models.DO_NOTHING, primary_key=True)
    rcategory = models.ForeignKey('Rsubcategories', models.DO_NOTHING)
    rsubcategory_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    translation = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brand_recipecatsubcategories'
        unique_together = (('brand_site', 'rcategory', 'rsubcategory_id'),)


class BrandRecipes(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    brand_site_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'brand_recipes'
        unique_together = (('recipe_id', 'brand_site_id'),)


class BrandRecipesBackupTemp(models.Model):
    recipe_id = models.IntegerField()
    brand_site_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'brand_recipes_backup_temp'


class BrandRecipesStg(models.Model):
    recipe_id = models.IntegerField()
    brand_site_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'brand_recipes_stg'


class BrandSite(models.Model):
    xref_brand_site_id = models.AutoField(primary_key=True)
    country = models.ForeignKey('Countries', models.DO_NOTHING)
    language = models.ForeignKey('Languages', models.DO_NOTHING)
    industry_sector = models.CharField(max_length=200)
    brand_site_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'brand_site'


class BrandSiteLinkMasks(models.Model):
    brand_id = models.IntegerField()
    language_id = models.IntegerField()
    recipe_link_mask = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brand_site_link_masks'


class BrandSiteTipSchedule(models.Model):
    brand_site_tip_schedule_id = models.AutoField(primary_key=True)
    active_month = models.IntegerField()
    active_day = models.IntegerField()
    final_month = models.IntegerField()
    final_day = models.IntegerField()
    brand_site = models.ForeignKey('Brands', models.DO_NOTHING)
    brand_site_tip = models.ForeignKey(BrandSiteTip, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'brand_site_tip_schedule'


class BrandTips(models.Model):
    brand_site = models.ForeignKey('Brands', models.DO_NOTHING, primary_key=True)
    tip_id = models.IntegerField()
    language_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'brand_tips'
        unique_together = (('brand_site', 'tip_id', 'language_id'),)


class BrandsBrandsite(models.Model):
    brand_id = models.IntegerField()
    brand_site_id = models.IntegerField()
    insertdate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'brands_brandsite'


class BuildKeywordMaster(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    keyword = models.CharField(max_length=60)
    canada = models.CharField(max_length=1, blank=True, null=True)
    kik = models.CharField(max_length=1, blank=True, null=True)
    comida = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'build_keyword_master'


class BuildRecipeKeywords(models.Model):
    keyword_id = models.IntegerField(primary_key=True)
    recipe_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'build_recipe_keywords'
        unique_together = (('keyword_id', 'recipe_id'),)


class CategoryFacets(models.Model):
    facetid = models.AutoField()
    ismemberfacet = models.IntegerField()
    categoryid = models.IntegerField(blank=True, null=True)
    subcategoryid = models.IntegerField(blank=True, null=True)
    facettypename = models.CharField(max_length=50, blank=True, null=True)
    facetname = models.CharField(max_length=50, blank=True, null=True)
    brandsiteid = models.IntegerField(blank=True, null=True)
    languageid = models.IntegerField(blank=True, null=True)
    status = models.NullBooleanField()
    dtcreated = models.DateTimeField(blank=True, null=True)
    dtmodified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'category_facets'


class CategoryGroupCategories(models.Model):
    category_group = models.ForeignKey('CategoryGroups', models.DO_NOTHING, primary_key=True)
    rcategory_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'category_group_categories'
        unique_together = (('category_group', 'rcategory_id'),)


class CategoryGroupSubcategories(models.Model):
    category_group_id = models.IntegerField(blank=True, null=True)
    rsubcategory_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'category_group_subcategories'


class ClassificationBitmaskValues(models.Model):
    brand_id = models.IntegerField()
    language_id = models.IntegerField()
    classification_type_id = models.IntegerField()
    bitmask_value = models.IntegerField()
    type_id = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'classification_bitmask_values'


class Classifications(models.Model):
    classification_type_id = models.AutoField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    classification_name = models.CharField(max_length=50)
    classification_precedence = models.IntegerField(blank=True, null=True)
    classification_icon = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'classifications'


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
        db_table = 'classificationstext'


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    photobytext = models.CharField(max_length=300, blank=True, null=True)
    copyrighttext = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'clients'


class Comidacrosslink(models.Model):
    crosslink_id = models.FloatField(db_column='crosslink id', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    title = models.CharField(max_length=255, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    f4 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'comidacrosslink$'


class CookingSchoolDictionary(models.Model):
    term_id = models.AutoField(primary_key=True)
    term = models.CharField(max_length=50)
    definition = models.CharField(max_length=7965)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'cooking_school_dictionary'


class Cookingmethods(models.Model):
    id = models.AutoField()
    methodname = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'cookingmethods'


class CrossLink(models.Model):
    cross_link_id = models.AutoField(primary_key=True)
    cross_link_placement_id = models.IntegerField()
    language_id = models.IntegerField()
    html = models.CharField(max_length=2500, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField()
    description = models.CharField(max_length=250, blank=True, null=True)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()
    status = models.CharField(max_length=1, blank=True, null=True)
    approved_name = models.CharField(max_length=250, blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cross_link'


class CrossLink18May15(models.Model):
    cross_link_id = models.AutoField()
    cross_link_placement_id = models.IntegerField()
    language_id = models.IntegerField()
    html = models.CharField(max_length=2500, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField()
    description = models.CharField(max_length=250, blank=True, null=True)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()
    status = models.CharField(max_length=1, blank=True, null=True)
    approved_name = models.CharField(max_length=250, blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cross_link_18may15'


class CrossLinkKeyword(models.Model):
    cross_link_keyword_id = models.AutoField(primary_key=True)
    cross_link_id = models.IntegerField()
    keyword = models.CharField(max_length=50)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'cross_link_keyword'


class CrossLinkPlacement(models.Model):
    cross_link_placement_id = models.AutoField(primary_key=True)
    cross_link_placement_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'cross_link_placement'


class Customtitle(models.Model):
    recipe = models.ForeignKey('KraftRecipes', models.DO_NOTHING)
    title = models.TextField(blank=True, null=True)
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'customtitle'


class Customtitle03182016(models.Model):
    recipe_id = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'customtitle03182016'


class DataSources(models.Model):
    data_source_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    dbname = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'data_sources'


class DwRecipeRitebites(models.Model):
    brand_site_id = models.IntegerField(blank=True, null=True)
    avg_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    entered_date = models.DateTimeField(blank=True, null=True)
    nbr_ingredients = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=1, blank=True, null=True)
    ready_in = models.IntegerField(blank=True, null=True)
    prep_time = models.IntegerField(blank=True, null=True)
    recipe_name = models.CharField(max_length=100, blank=True, null=True)
    rb14 = models.IntegerField(blank=True, null=True)
    rb13 = models.IntegerField(blank=True, null=True)
    rb11 = models.IntegerField(blank=True, null=True)
    rb9 = models.IntegerField(blank=True, null=True)
    rb8 = models.IntegerField(blank=True, null=True)
    rb7 = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    recipe_num = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    recipe_id = models.IntegerField(primary_key=True)
    rb50 = models.IntegerField(blank=True, null=True)
    rb51 = models.IntegerField(blank=True, null=True)
    rb52 = models.IntegerField(blank=True, null=True)
    rb53 = models.IntegerField(blank=True, null=True)
    rb54 = models.IntegerField(blank=True, null=True)
    rb60 = models.IntegerField(blank=True, null=True)
    rb61 = models.IntegerField(blank=True, null=True)
    rb62 = models.IntegerField(blank=True, null=True)
    rb63 = models.IntegerField(blank=True, null=True)
    rb64 = models.IntegerField(blank=True, null=True)
    insertdate = models.DateTimeField()
    kraft_rbs = models.IntegerField(blank=True, null=True)
    comida_rbs_en = models.IntegerField(blank=True, null=True)
    comida_rbs_sp = models.IntegerField(blank=True, null=True)
    sbd_recipe = models.NullBooleanField()
    canada_rbs_en = models.IntegerField(blank=True, null=True)
    canada_rbs_fr = models.IntegerField(blank=True, null=True)
    approved_flag = models.NullBooleanField()
    restricted_flag = models.NullBooleanField()
    times_rated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dw_recipe_ritebites'


class English(models.Model):
    cross_link_id = models.FloatField(db_column='cross link id', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=255, blank=True, null=True)
    html = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'english$'


class EntityLink(models.Model):
    entity_link_id = models.AutoField(primary_key=True)
    entity_id = models.IntegerField()
    entity_type_id = models.IntegerField()
    related_entity_id = models.IntegerField(blank=True, null=True)
    related_entity_type_id = models.IntegerField(blank=True, null=True)
    entity_priority = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()
    luname = models.CharField(max_length=50, blank=True, null=True)
    insertname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'entity_link'


class EntityType(models.Model):
    entity_type_id = models.AutoField(primary_key=True)
    entity_type_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'entity_type'


class FeaturedRecipes(models.Model):
    recipe_id = models.IntegerField()
    brand_site = models.ForeignKey(Brands, models.DO_NOTHING, primary_key=True)
    effective_date = models.DateTimeField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    termination_date = models.DateTimeField()
    header_image = models.CharField(max_length=300, blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)
    copy = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'featured_recipes'
        unique_together = (('brand_site', 'recipe_id', 'effective_date'),)


class French(models.Model):
    cross_link_id = models.FloatField(db_column='cross link id', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=255, blank=True, null=True)
    html = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'french$'


class GenericTip(models.Model):
    generic_tip_id = models.IntegerField()
    language_id = models.IntegerField()
    tip_title_name = models.CharField(max_length=200)
    status_ind = models.CharField(max_length=1)
    insert_date = models.DateTimeField(blank=True, null=True)
    ludate = models.DateTimeField(blank=True, null=True)
    display_on_web = models.NullBooleanField()
    country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'generic_tip'


class GenericTipAttribute(models.Model):
    generic_tip_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    generic_category_id = models.IntegerField()
    generic_subcategory_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'generic_tip_attribute'
        unique_together = (('generic_tip_id', 'language_id', 'generic_category_id', 'generic_subcategory_id'),)


class GenericTipBrand(models.Model):
    brand_site_id = models.IntegerField(primary_key=True)
    generic_tip_id = models.IntegerField()
    language_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'generic_tip_brand'
        unique_together = (('brand_site_id', 'generic_tip_id', 'language_id'),)


class GenericTipCategory(models.Model):
    generic_category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    generic_category_name = models.CharField(max_length=40)
    status_ind = models.CharField(max_length=1)
    cat_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'generic_tip_category'
        unique_together = (('generic_category_id', 'language_id'),)


class GenericTipCategoryBrand(models.Model):
    brand_site_id = models.IntegerField(primary_key=True)
    generic_category_id = models.IntegerField()
    language_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'generic_tip_category_brand'
        unique_together = (('brand_site_id', 'generic_category_id', 'language_id'),)


class GenericTipCategoryDesc(models.Model):
    generic_category_id = models.IntegerField()
    language_id = models.IntegerField()
    image = models.CharField(max_length=50)
    text_description = models.CharField(max_length=250)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'generic_tip_category_desc'


class GenericTipStep(models.Model):
    generic_tip_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    generic_tip_step_id = models.IntegerField()
    generic_tip_text = models.CharField(max_length=2000)
    sequence_num = models.IntegerField()
    country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'generic_tip_step'
        unique_together = (('generic_tip_id', 'language_id', 'generic_tip_step_id'),)


class GenericTipStepPhoto(models.Model):
    generic_tip_id = models.IntegerField()
    language_id = models.IntegerField()
    generic_tip_step_id = models.IntegerField()
    generic_tip_step_photo = models.CharField(max_length=50, blank=True, null=True)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'generic_tip_step_photo'


class GenericTipSubcategory(models.Model):
    generic_category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    generic_subcategory_id = models.IntegerField()
    generic_subcategory_name = models.CharField(max_length=40)
    status_ind = models.CharField(max_length=1)
    subcat_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'generic_tip_subcategory'
        unique_together = (('generic_category_id', 'language_id', 'generic_subcategory_id'),)


class GenericTipSubcategoryBrand(models.Model):
    brand_site_id = models.IntegerField(primary_key=True)
    generic_subcategory_id = models.IntegerField()
    language_id = models.IntegerField()
    generic_category_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'generic_tip_subcategory_brand'
        unique_together = (('brand_site_id', 'generic_subcategory_id', 'language_id', 'generic_category_id'),)


class GridColumnHeadings(models.Model):
    recipe_id = models.IntegerField()
    grid_column_heading_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    sequence_num = models.IntegerField(blank=True, null=True)
    grid_column_heading_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'grid_column_headings'
        unique_together = (('grid_column_heading_id', 'recipe_id'),)


class GridColumnDetails(models.Model):
    recipe_id = models.IntegerField()
    grid_column_heading = models.ForeignKey('GridColumnHeadings', models.DO_NOTHING, primary_key=True)
    grid_column_detail_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    sequence_num = models.IntegerField(blank=True, null=True)
    grid_column_detail_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'grid_column_details'
        unique_together = (('grid_column_heading', 'recipe_id', 'grid_column_detail_id'),)


class Groceryfacets(models.Model):
    ingredientid = models.FloatField(blank=True, null=True)
    ingredientname = models.CharField(max_length=255, blank=True, null=True)
    producttag = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'groceryfacets'


class IngredientFacets(models.Model):
    facetid = models.AutoField(primary_key=True)
    ismemberfacet = models.IntegerField()
    ingredientid = models.IntegerField(blank=True, null=True)
    facettypename = models.CharField(max_length=50, blank=True, null=True)
    facetname = models.CharField(max_length=50, blank=True, null=True)
    brandsiteid = models.IntegerField(blank=True, null=True)
    languageid = models.IntegerField(blank=True, null=True)
    status = models.NullBooleanField()
    dtcreated = models.DateTimeField(blank=True, null=True)
    dtmodified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredient_facets'


class IngredientKrl(models.Model):
    ingredient_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    krl_ingredient_id = models.IntegerField()
    language = models.ForeignKey('Languages', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'ingredient_krl'


class IngredientNutrio(models.Model):
    ingredient_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    nutrio_ingredient_id = models.IntegerField()
    language = models.ForeignKey('Languages', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'ingredient_nutrio'


class IngredientRolloverType(models.Model):
    ingredient_rollover_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'ingredient_rollover_type'


class IngredientRollover(models.Model):
    ingredient_rollover_id = models.AutoField(primary_key=True)
    ingredient_rollover_type = models.ForeignKey('IngredientRolloverType', models.DO_NOTHING)
    ingredient_id = models.IntegerField(blank=True, null=True)
    recipe_ingredient_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'ingredient_rollover'


class IngredientRolloverText(models.Model):
    ingredient_rollover_text_id = models.AutoField(primary_key=True)
    ingredient_rollover = models.ForeignKey(IngredientRollover, models.DO_NOTHING)
    language_id = models.IntegerField()
    link_url = models.CharField(max_length=255, blank=True, null=True)
    link_text = models.CharField(max_length=255, blank=True, null=True)
    headline = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    rollover_html = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'ingredient_rollover_text'


class IngredientSet(models.Model):
    ingredient_set_id = models.IntegerField(primary_key=True)
    recipe_id = models.IntegerField()
    primary = models.NullBooleanField()
    display_order = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    language_id = models.IntegerField()
    country_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ingredient_set'
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
        unique_together = (('ingredient_set_ingredient_id', 'language_id',
                            'country_id', 'ingredient_set_id', 'recipeid'),)


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
        db_table = 'ingredient_set_nutrition'


class IngredientType(models.Model):
    ingredient_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    display_order = models.IntegerField()
    display_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredient_type'


class Ingredients(models.Model):
    ingredient_id = models.AutoField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    language = models.ForeignKey('Languages', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    aisle = models.ForeignKey('ShoppingAisles', models.DO_NOTHING, blank=True, null=True)
    weights = models.CharField(max_length=50, blank=True, null=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    ingredient_name = models.CharField(max_length=255, blank=True, null=True)
    ingredient_text = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    formatted_ingredient_name = models.CharField(max_length=255, blank=True, null=True)
    ingredient_type = models.ForeignKey(IngredientTypeOld, models.DO_NOTHING, blank=True, null=True)
    ingredient_source_original_id = models.CharField(max_length=50, blank=True, null=True)
    gtin = models.CharField(max_length=50, blank=True, null=True)
    ingredient_source = models.ForeignKey(IngredientSource, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredients'


class Ingredients4142017(models.Model):
    ingredient_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    language_id = models.IntegerField()
    product_id = models.IntegerField(blank=True, null=True)
    aisle_id = models.IntegerField(blank=True, null=True)
    weights = models.CharField(max_length=50, blank=True, null=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    ingredient_name = models.CharField(max_length=255, blank=True, null=True)
    ingredient_text = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    formatted_ingredient_name = models.CharField(max_length=255, blank=True, null=True)
    ingredient_type_id = models.IntegerField(blank=True, null=True)
    ingredient_source_original_id = models.CharField(max_length=50, blank=True, null=True)
    gtin = models.CharField(max_length=50, blank=True, null=True)
    ingredient_source_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredients_4_14_2017'


class IngredientsJun122017(models.Model):
    ingredient_id = models.AutoField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    language_id = models.IntegerField()
    product_id = models.IntegerField(blank=True, null=True)
    aisle_id = models.IntegerField(blank=True, null=True)
    weights = models.CharField(max_length=50, blank=True, null=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    ingredient_name = models.CharField(max_length=255, blank=True, null=True)
    ingredient_text = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    formatted_ingredient_name = models.CharField(max_length=255, blank=True, null=True)
    ingredient_type_id = models.IntegerField(blank=True, null=True)
    ingredient_source_original_id = models.CharField(max_length=50, blank=True, null=True)
    gtin = models.CharField(max_length=50, blank=True, null=True)
    ingredient_source_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredients_jun_12_2017'


class IngredientsKeywords(models.Model):
    ingredient_id = models.IntegerField(primary_key=True)
    keywords = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredients_keywords'


class KraftRecipes03182016(models.Model):
    recipe_id = models.AutoField()
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
    yield_field = models.CharField(db_column='yield', max_length=150, blank=True, null=True)
    # Field renamed because it was a Python reserved word.
    skill_level = models.CharField(max_length=50, blank=True, null=True)
    number_of_servings = models.CharField(max_length=150, blank=True, null=True)
    nutrition_serving_size = models.CharField(max_length=80, blank=True, null=True)
    recipe_desc = models.CharField(max_length=100, blank=True, null=True)
    recipe_name = models.CharField(max_length=100, blank=True, null=True)
    nutrition_description = models.CharField(max_length=100, blank=True, null=True)
    grid_heading_text = models.CharField(max_length=500, blank=True, null=True)
    recipe_romance_text = models.CharField(max_length=500, blank=True, null=True)
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
    preparation_pretext = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kraft_recipes03182016'


class KraftRecipes03242016(models.Model):
    recipe_id = models.AutoField()
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
    yield_field = models.CharField(db_column='yield', max_length=150, blank=True, null=True)
    # Field renamed because it was a Python reserved word.
    skill_level = models.CharField(max_length=50, blank=True, null=True)
    number_of_servings = models.CharField(max_length=150, blank=True, null=True)
    nutrition_serving_size = models.CharField(max_length=80, blank=True, null=True)
    recipe_desc = models.CharField(max_length=100, blank=True, null=True)
    recipe_name = models.CharField(max_length=100, blank=True, null=True)
    nutrition_description = models.CharField(max_length=100, blank=True, null=True)
    grid_heading_text = models.CharField(max_length=500, blank=True, null=True)
    recipe_romance_text = models.CharField(max_length=500, blank=True, null=True)
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
    preparation_pretext = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kraft_recipes03242016'


class KraftRecipes03282016(models.Model):
    recipe_id = models.AutoField()
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
    yield_field = models.CharField(db_column='yield', max_length=150, blank=True, null=True)
    # Field renamed because it was a Python reserved word.
    skill_level = models.CharField(max_length=50, blank=True, null=True)
    number_of_servings = models.CharField(max_length=150, blank=True, null=True)
    nutrition_serving_size = models.CharField(max_length=80, blank=True, null=True)
    recipe_desc = models.CharField(max_length=100, blank=True, null=True)
    recipe_name = models.CharField(max_length=100, blank=True, null=True)
    nutrition_description = models.CharField(max_length=100, blank=True, null=True)
    grid_heading_text = models.CharField(max_length=500, blank=True, null=True)
    recipe_romance_text = models.CharField(max_length=500, blank=True, null=True)
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
    preparation_pretext = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kraft_recipes03282016'


class LastJobrunImageupload(models.Model):
    last_runtime = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'last_jobrun_imageupload'


class Loaddata(models.Model):
    ingredient = models.CharField(max_length=255, blank=True, null=True)
    brand_1_field = models.CharField(db_column='brand 1 ', max_length=255, blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    f3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'loaddata'


class MigrateTiming(models.Model):
    action = models.CharField(max_length=50)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField(blank=True, null=True)
    oldcount = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    newcount = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'migrate_timing'


class MtdAdditionalcontentmodule(models.Model):
    language_id = models.IntegerField()
    brand_site_id = models.IntegerField()
    itemdate = models.DateTimeField()
    imageurl = models.CharField(max_length=2000)
    imagelink = models.CharField(max_length=2000)
    titletext = models.CharField(max_length=2000)
    titleurl = models.CharField(max_length=2000)
    item1text = models.CharField(max_length=2000)
    item1url = models.CharField(max_length=2000)
    item2text = models.CharField(max_length=2000)
    item2url = models.CharField(max_length=2000)
    item3text = models.CharField(max_length=2000)
    item3url = models.CharField(max_length=2000)

    class Meta:
        managed = True
        db_table = 'mtd_additionalcontentmodule'


class Niq(models.Model):
    recipe_id = models.IntegerField()
    nutritional_item_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    quantity = models.CharField(max_length=50, blank=True, null=True)
    unit_of_measure = models.CharField(max_length=50, blank=True, null=True)
    prediscriptor = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'niq'


class NlCategoryLookups(models.Model):
    nl_category_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    display = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    nl_category_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'nl_category_lookups'


class NlProductExchanges(models.Model):
    nl_product_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    starch = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    fruit = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    milk_skim = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    milk_low_fat = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    milk_whole = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    other_carb = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    vegetable = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    meat_very_lean = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    meat_lean = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    meat_med_fat = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    meat_hi_fat = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    fat = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    free = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nl_product_exchanges'


class NlProducts(models.Model):
    nl_product_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    nl_brand = models.ForeignKey(NlBrandCategories, models.DO_NOTHING)
    nl_product_name = models.CharField(max_length=60)
    diabetic = models.CharField(max_length=2, blank=True, null=True)
    fat = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)
    serving_size = models.CharField(max_length=50, blank=True, null=True)
    flavor = models.CharField(max_length=80, blank=True, null=True)
    carbs = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nl_products'


class NutritionInfo(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    nutrition_exchange_item_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    diet_exchange = models.CharField(max_length=500, blank=True, null=True)
    nutrition_bonus = models.CharField(max_length=2000, blank=True, null=True)
    carb_counter = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nutrition_info'
        unique_together = (('recipe_id', 'nutrition_exchange_item_id'),)


class NutritionReference(models.Model):
    nutrition_reference_id = models.IntegerField(primary_key=True)
    nutrition_reference_name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    insertdate = models.DateTimeField(blank=True, null=True)
    ludate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nutrition_reference'


class NutritionReferenceUnit(models.Model):
    nutrition_reference_unit_id = models.IntegerField(primary_key=True)
    nutrition_reference_unit_name = models.CharField(max_length=25, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    insertdate = models.DateTimeField(blank=True, null=True)
    ludate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nutrition_reference_unit'


class NutritionalItemQuantities(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    nutritional_item_id = models.IntegerField()
    nutrition_exchange_item_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    quantity = models.CharField(max_length=50, blank=True, null=True)
    unit_of_measure = models.CharField(max_length=50, blank=True, null=True)
    prediscriptor = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nutritional_item_quantities'
        unique_together = (('recipe_id', 'nutritional_item_id', 'nutrition_exchange_item_id'),)


class NutritionalItems(models.Model):
    nutritional_item_id = models.AutoField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    language = models.ForeignKey(Languages, models.DO_NOTHING, blank=True, null=True)
    unit_of_measure = models.CharField(max_length=10, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    nutritional_item_type = models.CharField(max_length=50, blank=True, null=True)
    nutritional_document = models.CharField(max_length=128, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    nutrient_short_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nutritional_items'


class OrgRecipeMap(models.Model):
    new_id = models.CharField(max_length=50, blank=True, null=True)
    old_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'org_recipe_map'


class ProductsTemp(models.Model):
    product_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    product_location = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    product_category_id = models.IntegerField()
    brand_site_id = models.IntegerField(blank=True, null=True)
    hyper_link = models.CharField(max_length=100, blank=True, null=True)
    product_title = models.CharField(max_length=120, blank=True, null=True)
    product_description = models.CharField(max_length=7500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'products_temp'


class Rcategories(models.Model):
    rcategory_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    brand_site_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField()
    cat_rank = models.IntegerField()
    rcategory = models.CharField(max_length=80)

    class Meta:
        managed = True
        db_table = 'rcategories'


class RecipeBanner(models.Model):
    recipe_banner_id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(KraftRecipes, models.DO_NOTHING)
    banner = models.ForeignKey(Banner, models.DO_NOTHING)
    custom_banner = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    dtcreated = models.DateTimeField()
    createdbyuser = models.IntegerField()
    dtupdated = models.DateTimeField()
    updatedbyuser = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'recipe_banner'


class RecipeCategorySubcategories(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    rcategory_id = models.IntegerField()
    rsubcategory_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'recipe_category_subcategories'
        unique_together = (('recipe_id', 'rcategory_id', 'rsubcategory_id'),)


class RecipeClassifications(models.Model):
    recipe_id = models.IntegerField()
    classification_type_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    classification_category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_classifications'


class RecipeClient(models.Model):
    recipeclientid = models.AutoField(primary_key=True)
    recipe_id = models.IntegerField()
    client_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'recipe_client'


class RecipeFormat(models.Model):
    recipe_format_id = models.IntegerField(primary_key=True)
    recipe_format_name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    ludate_field = models.DateTimeField(db_column='ludate ', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    insertdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_format'


class RecipeGenericTip(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    generic_tip_id = models.IntegerField()
    language_id = models.IntegerField()
    sequence_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'recipe_generic_tip'
        unique_together = (('recipe_id', 'generic_tip_id', 'language_id'),)


class RecipeImageType(models.Model):
    recipe_image_type_id = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    ludate = models.DateTimeField(blank=True, null=True)
    insertdate = models.DateTimeField(blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    width = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_image_type'


class RecipeIngredientAttribute(models.Model):
    recipe_ingredient_attribute_id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey(Attribute, models.DO_NOTHING)
    recipe_ingredient_id = models.IntegerField(blank=True, null=True)
    attribute_value = models.CharField(max_length=20, blank=True, null=True)
    dtcreated = models.DateTimeField(blank=True, null=True)
    createdbyuser = models.IntegerField(blank=True, null=True)
    dtupdated = models.DateTimeField(blank=True, null=True)
    updatedbyuser = models.IntegerField(blank=True, null=True)
    ingredient_set_ingredient_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_ingredient_attribute'


class RecipeIngredientLinkAttribute(models.Model):
    recipe_ingredient_link_attribute_id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey(Attribute, models.DO_NOTHING)
    recipe_ingredient_link_id = models.IntegerField()
    attribute_value = models.CharField(max_length=20, blank=True, null=True)
    dtcreated = models.DateTimeField(blank=True, null=True)
    createdbyuser = models.DateTimeField(blank=True, null=True)
    dtupdated = models.DateTimeField(blank=True, null=True)
    updatedbyuser = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
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
        db_table = 'recipe_ingredient_links'


class RecipeIngredientLinks03022016(models.Model):
    recipe_ingredient_link_id = models.AutoField()
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
        db_table = 'recipe_ingredient_links_03022016'


class RecipeIngredientLinks03102016(models.Model):
    recipe_ingredient_link_id = models.AutoField()
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
        db_table = 'recipe_ingredient_links_03102016'


class RecipeIngredientLinks03152016(models.Model):
    recipe_ingredient_link_id = models.AutoField()
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
        db_table = 'recipe_ingredient_links_03152016'


class RecipeIngredientLinks03162016(models.Model):
    recipe_ingredient_link_id = models.AutoField()
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
        db_table = 'recipe_ingredient_links_03162016'


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
        db_table = 'recipe_ingredients'


class RecipeIngredientsHeading(models.Model):
    recipe_id = models.IntegerField()
    ingredient_heading_id = models.IntegerField()
    ingredient_heading_text = models.CharField(max_length=510, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_ingredients_heading'


class RecipeIngredientsHeadingBackupForkrlissues(models.Model):
    recipe_id = models.IntegerField()
    ingredient_heading_id = models.IntegerField()
    ingredient_heading_text = models.CharField(max_length=510, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_ingredients_heading_backup_forkrlissues'


class RecipeKeywords(models.Model):
    recipe_id = models.IntegerField()
    keyword_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'recipe_keywords'
        unique_together = (('keyword_id', 'recipe_id'),)


class RecipeKrl(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    krl_recipe_id = models.IntegerField()
    language = models.ForeignKey(Languages, models.DO_NOTHING)
    variation_id = models.IntegerField()
    level_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'recipe_krl'


class RecipeMap(models.Model):
    new_id = models.IntegerField()
    old_id = models.CharField(max_length=20)
    entered_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_map'


class RecipeNutrio(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    nutrio_recipe_id = models.IntegerField()
    language = models.ForeignKey(Languages, models.DO_NOTHING)

    class Meta:
        managed = True
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
        db_table = 'recipe_photos'


class RecipePhotos042220156PmBkup(models.Model):
    recipe_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)
    recipe_image_type_id = models.IntegerField(blank=True, null=True)
    sequence_char = models.CharField(max_length=10, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    recipe_photos_id = models.AutoField()
    author = models.CharField(max_length=30, blank=True, null=True)
    image_type = models.CharField(max_length=20, blank=True, null=True)
    mime_type = models.CharField(max_length=20, blank=True, null=True)
    image_rendition = models.CharField(max_length=15, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_photos_04_22_2015_6pm_bkup'


class RecipePhotos07012015(models.Model):
    recipe_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)
    recipe_image_type_id = models.IntegerField(blank=True, null=True)
    sequence_char = models.CharField(max_length=10, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    recipe_photos_id = models.AutoField()
    author = models.CharField(max_length=30, blank=True, null=True)
    image_type = models.CharField(max_length=20, blank=True, null=True)
    mime_type = models.CharField(max_length=20, blank=True, null=True)
    image_rendition = models.CharField(max_length=15, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_photos_07012015'


class RecipePhotosBkp(models.Model):
    recipe_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)
    recipe_image_type_id = models.IntegerField(blank=True, null=True)
    sequence_char = models.CharField(max_length=10, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    recipe_photos_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'recipe_photos_bkp'


class RecipePhotosBkup04241022Am(models.Model):
    recipe_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)
    recipe_image_type_id = models.IntegerField(blank=True, null=True)
    sequence_char = models.CharField(max_length=10, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    recipe_photos_id = models.AutoField()
    author = models.CharField(max_length=30, blank=True, null=True)
    image_type = models.CharField(max_length=20, blank=True, null=True)
    mime_type = models.CharField(max_length=20, blank=True, null=True)
    image_rendition = models.CharField(max_length=15, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_photos_bkup_04_24_10_22am'


class RecipePhotosImportlog(models.Model):
    recipe_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)
    recipe_image_type_id = models.IntegerField(blank=True, null=True)
    sequence_char = models.CharField(max_length=10, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    image_type = models.CharField(max_length=20, blank=True, null=True)
    mime_type = models.CharField(max_length=20, blank=True, null=True)
    image_rendition = models.CharField(max_length=15, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    result = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=900, blank=True, null=True)
    recipe_photos_id = models.IntegerField(blank=True, null=True)
    recipe_photos_log_id = models.AutoField()
    rerundate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_photos_importlog'


class RecipePhotosPluck(models.Model):
    recipe_photos_pluck_id = models.IntegerField()
    siteid = models.IntegerField()
    userid = models.IntegerField()
    recipe_id = models.IntegerField()
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)
    recipe_image_type_id = models.IntegerField(blank=True, null=True)
    image_rendition = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_photos_pluck'


class RecipePhotosTempBackup(models.Model):
    recipe_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)
    recipe_image_type_id = models.IntegerField(blank=True, null=True)
    sequence_char = models.CharField(max_length=10, blank=True, null=True)
    sequence_num = models.IntegerField(blank=True, null=True)
    recipe_photos_id = models.IntegerField()
    author = models.CharField(max_length=30, blank=True, null=True)
    image_type = models.CharField(max_length=20, blank=True, null=True)
    mime_type = models.CharField(max_length=20, blank=True, null=True)
    image_rendition = models.CharField(max_length=15, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_photos_temp_backup'


class RecipeProducts(models.Model):
    recipe_id = models.IntegerField()
    product = models.ForeignKey(Products, models.DO_NOTHING, primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'recipe_products'
        unique_together = (('product', 'recipe_id'),)


class RecipeSearchFlat(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    search_text = models.CharField(max_length=4000, blank=True, null=True)
    language_id = models.IntegerField()
    brand_site_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'recipe_search_flat'


class RecipeSearchFlat6162017(models.Model):
    recipe_id = models.IntegerField()
    search_text = models.CharField(max_length=4000, blank=True, null=True)
    language_id = models.IntegerField()
    brand_site_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'recipe_search_flat_6_16_2017'


class RecipeSearchFlatVariable(models.Model):
    varrecipeid = models.IntegerField(blank=True, null=True)
    varsearchtext = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_search_flat_variable'


class RecipeSpecificTip(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    recipe_specific_tip_id = models.IntegerField()
    tip_title_name = models.CharField(max_length=200, blank=True, null=True)
    recipe_specific_tip_text = models.CharField(max_length=2000, blank=True, null=True)
    sequence_id = models.IntegerField(blank=True, null=True)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'recipe_specific_tip'
        unique_together = (('recipe_id', 'recipe_specific_tip_id'),)


class RecipeSubcategoryList(models.Model):
    recipe_subcategory_list_id = models.AutoField(primary_key=True)
    recipe_id = models.IntegerField()
    meal_part = models.CharField(max_length=1000, blank=True, null=True)
    day_part = models.CharField(max_length=1000, blank=True, null=True)
    product_brand = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_subcategory_list'
        unique_together = (('recipe_subcategory_list_id', 'recipe_id'),)


class RecipeTaxonomy(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    taxonomy_id = models.IntegerField()
    insert_date = models.DateTimeField()
    ludate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe_taxonomy'
        unique_together = (('recipe_id', 'taxonomy_id'),)


class RecipeTips(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    tip = models.ForeignKey('Tips', models.DO_NOTHING)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    sequence_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'recipe_tips'
        unique_together = (('recipe_id', 'tip'),)


class RecipeTrademarks(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    trademark_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    language_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'recipe_trademarks'
        unique_together = (('recipe_id', 'trademark_id', 'language_id'),)


class RecipeTranslations(models.Model):
    from_recipe_id = models.IntegerField(primary_key=True)
    to_recipe_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'recipe_translations'
        unique_together = (('from_recipe_id', 'to_recipe_id'),)


class RecipeType(models.Model):
    recipe_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = True
        db_table = 'recipe_type'


class Reciperelation(models.Model):
    reciperelationid = models.AutoField(primary_key=True)
    relationid = models.IntegerField()
    recipe_id = models.IntegerField()
    brand_site_id = models.IntegerField()
    language_id = models.IntegerField()
    status = models.NullBooleanField()
    dtcreated = models.DateTimeField(blank=True, null=True)
    createdbyuser = models.IntegerField(blank=True, null=True)
    dtupdated = models.DateTimeField(blank=True, null=True)
    updatedbyuser = models.IntegerField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reciperelation'


class RelatedRecipes(models.Model):
    related_recipe_id = models.IntegerField(primary_key=True)
    recipe_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'related_recipes'
        unique_together = (('related_recipe_id', 'recipe_id'),)


class Relation(models.Model):
    relationid = models.AutoField(primary_key=True)
    relationtypeid = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    descr = models.CharField(max_length=250)
    repeating = models.BooleanField()
    status = models.NullBooleanField()
    dtcreated = models.DateTimeField(blank=True, null=True)
    createdbyuser = models.IntegerField(blank=True, null=True)
    dtupdated = models.DateTimeField(blank=True, null=True)
    updatedbyuser = models.CharField(max_length=10, blank=True, null=True)
    item = models.CharField(max_length=255, blank=True, null=True)
    itempath = models.CharField(max_length=255, blank=True, null=True)
    itemurl = models.CharField(max_length=255, blank=True, null=True)
    itemheight = models.IntegerField(blank=True, null=True)
    itemwidth = models.IntegerField(blank=True, null=True)
    itemtext = models.CharField(max_length=500, blank=True, null=True)
    itemsize = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'relation'


class Relationtype(models.Model):
    relationtypeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    descr = models.CharField(max_length=250, blank=True, null=True)
    status = models.NullBooleanField()
    dtcreated = models.DateTimeField(blank=True, null=True)
    createdbyuser = models.IntegerField(blank=True, null=True)
    dtupdated = models.DateTimeField(blank=True, null=True)
    updatedbyuser = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'relationtype'


class Resource(models.Model):
    resource_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resource'


class RiaRecipe(models.Model):
    rank_top10_overall = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    rank_top10_weekly = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    user2_date_rated = models.DateTimeField(blank=True, null=True)
    user1_date_rated = models.DateTimeField(blank=True, null=True)
    user2_comment = models.CharField(max_length=2000, blank=True, null=True)
    user1_comment = models.CharField(max_length=2000, blank=True, null=True)
    user2_rating = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    user1_rating = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    percent_make_it_again = models.DecimalField(max_digits=3, decimal_places=0)
    avg_rating = models.DecimalField(max_digits=2, decimal_places=1)
    recipe_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'ria_recipe'


class RiaRecipeStage(models.Model):
    load = models.ForeignKey(RiaLoadHistory, models.DO_NOTHING)
    load_date = models.DateTimeField()
    recipe_id = models.CharField(max_length=20)
    user1_date_rated = models.DateTimeField(blank=True, null=True)
    user2_date_rated = models.DateTimeField(blank=True, null=True)
    user1_rating = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    user2_rating = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    avg_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    rank_top10_weekly = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    percent_make_it_again = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    rank_top10_overall = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    user1_comment = models.CharField(max_length=2000, blank=True, null=True)
    user2_comment = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ria_recipe_stage'


class RiaUserRating(models.Model):
    user_nbr = models.DecimalField(max_digits=8, decimal_places=0)
    recipe_id = models.IntegerField()
    user_rating = models.DecimalField(max_digits=1, decimal_places=0)
    user_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'ria_user_rating'


class RiaUserRatingBad(models.Model):
    load_id = models.DecimalField(max_digits=9, decimal_places=0)
    load_date = models.DateTimeField()
    user_nbr = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    recipe_id = models.IntegerField(blank=True, null=True)
    user_rating = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ria_user_rating_bad'


class RiaUserRatingStage(models.Model):
    load_id = models.DecimalField(max_digits=9, decimal_places=0)
    load_date = models.DateTimeField()
    user_nbr = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    recipe_id = models.IntegerField(blank=True, null=True)
    user_rating = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ria_user_rating_stage'


class Rotd(models.Model):
    recipe_id = models.IntegerField()
    date_to_display = models.DateTimeField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    order_nbr = models.IntegerField(blank=True, null=True)
    personalize = models.IntegerField()
    rating_comment = models.CharField(max_length=2000, blank=True, null=True)
    rating_author = models.CharField(max_length=100, blank=True, null=True)
    language_id = models.IntegerField()
    brand_site_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'rotd'
        unique_together = (('date_to_display', 'personalize', 'brand_site_id', 'language_id'),)


class Rotm(models.Model):
    brand_site = models.ForeignKey(Brands, models.DO_NOTHING)
    month = models.CharField(primary_key=True, max_length=4)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    effective_date = models.DateTimeField()
    termination_date = models.DateTimeField()
    recipe_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'rotm'
        unique_together = (('month', 'brand_site'),)


class Rotw(models.Model):
    effective_date = models.DateTimeField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    termination_date = models.DateTimeField()
    recipe_id = models.IntegerField()
    brand_site = models.ForeignKey(Brands, models.DO_NOTHING)
    language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = True
        db_table = 'rotw'
        unique_together = (('language', 'effective_date'),)


class Sharepointsitelist(models.Model):
    siteid = models.IntegerField()
    sitename = models.CharField(max_length=50)
    siteurl = models.CharField(max_length=100)
    contentdatabase = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'sharepointsitelist'


class SnackTips(models.Model):
    snack_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    photo = models.CharField(max_length=1)
    snack_title = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'snack_tips'		


class SnackPreps(models.Model):
    snack = models.ForeignKey('SnackTips', models.DO_NOTHING, primary_key=True)
    step_num = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    prep = models.CharField(max_length=2000)

    class Meta:
        managed = True
        db_table = 'snack_preps'
        unique_together = (('snack', 'step_num'),)


class Sotw(models.Model):
    effective_date = models.DateTimeField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    termination_date = models.DateTimeField()
    snack = models.ForeignKey(SnackTips, models.DO_NOTHING)
    personalize = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sotw'


class SpecialOccasionRecipes(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    special_occasion = models.ForeignKey('SpecialOccasions', models.DO_NOTHING)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'special_occasion_recipes'
        unique_together = (('recipe_id', 'special_occasion'),)


class Sponsoredlinkstage2(models.Model):
    cross_link_id = models.IntegerField(db_column='cross link id', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    updated = models.CharField(max_length=50, blank=True, null=True)
    html = models.CharField(max_length=5000, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sponsoredlinkstage2'


class StateCodes(models.Model):
    state_code = models.CharField(primary_key=True, max_length=2)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    state_name = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'state_codes'


class Staticrecipesearch(models.Model):
    staticrecipesearch_id = models.AutoField()
    staticrecipesearchname = models.CharField(max_length=50)
    brand_id = models.IntegerField()
    language_id = models.IntegerField()
    sortfield = models.CharField(max_length=50, blank=True, null=True)
    sortdirection = models.CharField(max_length=10, blank=True, null=True)
    start = models.IntegerField()
    end = models.IntegerField()
    ingredients = models.CharField(max_length=1000, blank=True, null=True)
    term1 = models.CharField(max_length=50, blank=True, null=True)
    term2 = models.CharField(max_length=50, blank=True, null=True)
    term3 = models.CharField(max_length=50, blank=True, null=True)
    term4 = models.CharField(max_length=50, blank=True, null=True)
    term5 = models.CharField(max_length=50, blank=True, null=True)
    term6 = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    subtype = models.IntegerField(blank=True, null=True)
    classifications = models.CharField(max_length=500, blank=True, null=True)
    displaynonapproved = models.NullBooleanField()
    featured = models.NullBooleanField()
    ignorefeaturedrecipeid = models.IntegerField(blank=True, null=True)
    displayrestricted = models.NullBooleanField()
    catgroupids = models.CharField(max_length=100, blank=True, null=True)
    types = models.CharField(max_length=100, blank=True, null=True)
    subtypes = models.CharField(max_length=100, blank=True, null=True)
    recipephotorequired = models.NullBooleanField()
    excludekeyword = models.CharField(max_length=50, blank=True, null=True)
    excluderecipeids = models.CharField(max_length=120, blank=True, null=True)
    minratingcount = models.IntegerField(blank=True, null=True)
    minrecipeentereddate = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'staticrecipesearch'


class Swaps(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    submitters_name = models.CharField(max_length=200, blank=True, null=True)
    submitters_address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'swaps'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Taxonomy(models.Model):
    taxonomy_type = models.ForeignKey('TaxonomyType', models.DO_NOTHING, blank=True, null=True)
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
        unique_together = (('taxonomy_id', 'country_id', 'language_id'),)


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
        db_table = 'taxonomy_type_resource'


class TblPhillyRecipes(models.Model):
    recipe_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    sc_id1 = models.IntegerField(blank=True, null=True)
    sc_id2 = models.IntegerField(blank=True, null=True)
    sc_id3 = models.IntegerField(blank=True, null=True)
    sc_id4 = models.IntegerField(blank=True, null=True)
    sc_id5 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_philly_recipes'


class TblPhillyRecipesKeywords(models.Model):
    recipe_id = models.IntegerField(blank=True, null=True)
    key_id1 = models.IntegerField(blank=True, null=True)
    key_id2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_philly_recipes_keywords'


class TempIngredientFacetImport(models.Model):
    id = models.CharField(max_length=500, blank=True, null=True)
    ingredientname = models.CharField(max_length=1000, blank=True, null=True)
    facetname1 = models.CharField(max_length=500, blank=True, null=True)
    facetname2 = models.CharField(max_length=500, blank=True, null=True)
    facetname3 = models.CharField(max_length=500, blank=True, null=True)
    facetname4 = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'temp_ingredient_facet_import'


class Tempsitemap(models.Model):
    loc = models.CharField(max_length=300, blank=True, null=True)
    lastmod = models.CharField(max_length=30, blank=True, null=True)
    changefreq = models.CharField(max_length=10, blank=True, null=True)
    priority = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tempsitemap'


class Tempsitemaphttpstatus(models.Model):
    statuscode = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tempsitemaphttpstatus'


class Test(models.Model):
    id = models.IntegerField(blank=True, null=True)
    col = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'test'


class Testssispackage(models.Model):
    testid = models.AutoField()
    testname = models.CharField(max_length=50)
    createddate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'testssispackage'


class TipCategorySubcategories(models.Model):
    tcategory = models.ForeignKey('Tsubcategories', models.DO_NOTHING)
    tsubcategory_id = models.IntegerField(blank=True, null=True)
    tip = models.ForeignKey('Tips', models.DO_NOTHING)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'tip_category_subcategories'


class TipKeywords(models.Model):
    keyword = models.ForeignKey(KeywordMaster, models.DO_NOTHING)
    tip = models.ForeignKey('Tips', models.DO_NOTHING, primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'tip_keywords'
        unique_together = (('tip', 'keyword'),)


class TipSteps(models.Model):
    tip = models.ForeignKey('Tips', models.DO_NOTHING, primary_key=True)
    step_order = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    tip_step_description = models.CharField(max_length=2000)
    tip_step_image_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tip_steps'
        unique_together = (('tip', 'step_order'),)


class TipPhotos(models.Model):
    tip_photo_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    step_order = models.IntegerField()
    tip = models.ForeignKey('TipSteps', models.DO_NOTHING)
    photo_filename = models.CharField(max_length=250)
    photo_directory = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tip_photos'


class TipText(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    sequence_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    tip_text = models.CharField(max_length=2000)

    class Meta:
        managed = True
        db_table = 'tip_text'
        unique_together = (('recipe_id', 'sequence_id'),)


class TmpRecipeingredients(models.Model):
    recipeid = models.IntegerField()
    ingredient_step = models.IntegerField(blank=True, null=True)
    ingredients = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tmp_recipeingredients'


class TmpRecipeingredientsall(models.Model):
    recipeid = models.IntegerField()
    ingred_1 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_2 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_3 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_4 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_5 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_6 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_7 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_8 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_9 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_10 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_11 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_12 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_13 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_14 = models.CharField(max_length=2000, blank=True, null=True)
    ingred_15 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tmp_recipeingredientsall'


class TmpReciperating(models.Model):
    recipeid = models.IntegerField()
    rating = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    numberofratings = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tmp_reciperating'


class Trademarks(models.Model):
    trademark_id = models.IntegerField()
    status = models.CharField(max_length=1)
    insertdate = models.DateTimeField()
    ludate = models.DateTimeField()
    language = models.ForeignKey(Languages, models.DO_NOTHING)
    trademark_description = models.CharField(max_length=500)
    country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'trademarks'


class Unit(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    full_name = models.CharField(max_length=100, blank=True, null=True)
    abbreviation = models.CharField(max_length=100, blank=True, null=True)
    country_id = models.IntegerField()
    status = models.CharField(max_length=1)
    abbreviation_plural = models.CharField(max_length=50, blank=True, null=True)
    full_name_plural = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'unit'
        unique_together = (('unit_id', 'country_id', 'language_id'),)


class Updatedrecipes(models.Model):
    id = models.AutoField()
    recipe_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'updatedrecipes'


class Updatedrecipes1(models.Model):
    id = models.AutoField()
    recipe_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'updatedrecipes1'


class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    video_type_id = models.IntegerField()
    video_name = models.CharField(max_length=150)
    video_url_1 = models.CharField(max_length=250, blank=True, null=True)
    video_url_2 = models.CharField(max_length=250, blank=True, null=True)
    video_url_3 = models.CharField(max_length=250, blank=True, null=True)
    video_url_4 = models.CharField(max_length=250, blank=True, null=True)
    video_description = models.CharField(max_length=250, blank=True, null=True)
    video_instructions_url = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()
    aspect_ratio = models.CharField(max_length=10)
    thumbnail_img = models.CharField(max_length=250, blank=True, null=True)
    video_time = models.CharField(max_length=20, blank=True, null=True)
    video_memo = models.CharField(max_length=5000, blank=True, null=True)
    intro_img = models.CharField(max_length=250, blank=True, null=True)
    video_url_5 = models.CharField(max_length=250, blank=True, null=True)
    video_sponsored_by_brandid = models.IntegerField(blank=True, null=True)
    videopath = models.CharField(max_length=250, blank=True, null=True)
    video_iphone_high = models.CharField(max_length=250, blank=True, null=True)
    video_iphone_low = models.CharField(max_length=250, blank=True, null=True)
    video_preroll1 = models.CharField(max_length=250, blank=True, null=True)
    video_preroll2 = models.CharField(max_length=250, blank=True, null=True)
    video_tableturl = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=50, blank=True, null=True)
    brightcove_video_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'video'


class VideoAttribute(models.Model):
    video_id = models.IntegerField(primary_key=True)
    video_category_id = models.IntegerField()
    video_subcategory_id = models.IntegerField()
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'video_attribute'
        unique_together = (('video_id', 'video_category_id', 'video_subcategory_id'),)


class VideoBackupTemp(models.Model):
    video_id = models.IntegerField()
    language_id = models.IntegerField()
    video_type_id = models.IntegerField()
    video_name = models.CharField(max_length=150)
    video_url_1 = models.CharField(max_length=250, blank=True, null=True)
    video_url_2 = models.CharField(max_length=250, blank=True, null=True)
    video_url_3 = models.CharField(max_length=250, blank=True, null=True)
    video_url_4 = models.CharField(max_length=250, blank=True, null=True)
    video_description = models.CharField(max_length=250, blank=True, null=True)
    video_instructions_url = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()
    aspect_ratio = models.CharField(max_length=10)
    thumbnail_img = models.CharField(max_length=250, blank=True, null=True)
    video_time = models.CharField(max_length=20, blank=True, null=True)
    video_memo = models.CharField(max_length=5000, blank=True, null=True)
    intro_img = models.CharField(max_length=250, blank=True, null=True)
    video_url_5 = models.CharField(max_length=250, blank=True, null=True)
    video_sponsored_by_brandid = models.IntegerField(blank=True, null=True)
    videopath = models.CharField(max_length=250, blank=True, null=True)
    video_iphone_high = models.CharField(max_length=250, blank=True, null=True)
    video_iphone_low = models.CharField(max_length=250, blank=True, null=True)
    video_preroll1 = models.CharField(max_length=250, blank=True, null=True)
    video_preroll2 = models.CharField(max_length=250, blank=True, null=True)
    video_tableturl = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=50, blank=True, null=True)
    brightcove_video_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'video_backup_temp'


class VideoBkp5May15(models.Model):
    video_id = models.AutoField()
    language_id = models.IntegerField()
    video_type_id = models.IntegerField()
    video_name = models.CharField(max_length=150)
    video_url_1 = models.CharField(max_length=250, blank=True, null=True)
    video_url_2 = models.CharField(max_length=250, blank=True, null=True)
    video_url_3 = models.CharField(max_length=250, blank=True, null=True)
    video_url_4 = models.CharField(max_length=250, blank=True, null=True)
    video_description = models.CharField(max_length=250, blank=True, null=True)
    video_instructions_url = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()
    aspect_ratio = models.CharField(max_length=10)
    thumbnail_img = models.CharField(max_length=250, blank=True, null=True)
    video_time = models.CharField(max_length=20, blank=True, null=True)
    video_memo = models.CharField(max_length=5000, blank=True, null=True)
    intro_img = models.CharField(max_length=250, blank=True, null=True)
    video_url_5 = models.CharField(max_length=250, blank=True, null=True)
    video_sponsored_by_brandid = models.IntegerField(blank=True, null=True)
    videopath = models.CharField(max_length=250, blank=True, null=True)
    video_iphone_high = models.CharField(max_length=250, blank=True, null=True)
    video_iphone_low = models.CharField(max_length=250, blank=True, null=True)
    video_preroll1 = models.CharField(max_length=250, blank=True, null=True)
    video_preroll2 = models.CharField(max_length=250, blank=True, null=True)
    video_tableturl = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=50, blank=True, null=True)
    brightcove_video_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'video_bkp_5may15'


class VideoBkup(models.Model):
    video_id = models.AutoField()
    language_id = models.IntegerField()
    video_type_id = models.IntegerField()
    video_name = models.CharField(max_length=150)
    video_url_1 = models.CharField(max_length=250, blank=True, null=True)
    video_url_2 = models.CharField(max_length=250, blank=True, null=True)
    video_url_3 = models.CharField(max_length=250, blank=True, null=True)
    video_url_4 = models.CharField(max_length=250, blank=True, null=True)
    video_description = models.CharField(max_length=250, blank=True, null=True)
    video_instructions_url = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()
    aspect_ratio = models.CharField(max_length=10)
    thumbnail_img = models.CharField(max_length=250, blank=True, null=True)
    video_time = models.CharField(max_length=20, blank=True, null=True)
    video_memo = models.CharField(max_length=5000, blank=True, null=True)
    intro_img = models.CharField(max_length=250, blank=True, null=True)
    video_url_5 = models.CharField(max_length=250, blank=True, null=True)
    video_sponsored_by_brandid = models.IntegerField(blank=True, null=True)
    videopath = models.CharField(max_length=250, blank=True, null=True)
    video_iphone_high = models.CharField(max_length=250, blank=True, null=True)
    video_iphone_low = models.CharField(max_length=250, blank=True, null=True)
    video_preroll1 = models.CharField(max_length=250, blank=True, null=True)
    video_preroll2 = models.CharField(max_length=250, blank=True, null=True)
    video_tableturl = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=50, blank=True, null=True)
    brightcove_video_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'video_bkup'


class VideoBkup0520(models.Model):
    video_id = models.AutoField()
    language_id = models.IntegerField()
    video_type_id = models.IntegerField()
    video_name = models.CharField(max_length=150)
    video_url_1 = models.CharField(max_length=250, blank=True, null=True)
    video_url_2 = models.CharField(max_length=250, blank=True, null=True)
    video_url_3 = models.CharField(max_length=250, blank=True, null=True)
    video_url_4 = models.CharField(max_length=250, blank=True, null=True)
    video_description = models.CharField(max_length=250, blank=True, null=True)
    video_instructions_url = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()
    aspect_ratio = models.CharField(max_length=10)
    thumbnail_img = models.CharField(max_length=250, blank=True, null=True)
    video_time = models.CharField(max_length=20, blank=True, null=True)
    video_memo = models.CharField(max_length=5000, blank=True, null=True)
    intro_img = models.CharField(max_length=250, blank=True, null=True)
    video_url_5 = models.CharField(max_length=250, blank=True, null=True)
    video_sponsored_by_brandid = models.IntegerField(blank=True, null=True)
    videopath = models.CharField(max_length=250, blank=True, null=True)
    video_iphone_high = models.CharField(max_length=250, blank=True, null=True)
    video_iphone_low = models.CharField(max_length=250, blank=True, null=True)
    video_preroll1 = models.CharField(max_length=250, blank=True, null=True)
    video_preroll2 = models.CharField(max_length=250, blank=True, null=True)
    video_tableturl = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=50, blank=True, null=True)
    brightcove_video_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'video_bkup_05_20'


class VideoCategory(models.Model):
    video_category_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    brand_id = models.IntegerField()
    video_type_id = models.IntegerField()
    video_category_name = models.CharField(max_length=50, blank=True, null=True)
    video_category_description = models.CharField(max_length=250, blank=True, null=True)
    video_category_image = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'video_category'


class VideoSubcategory(models.Model):
    video_subcategory_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    brand_id = models.IntegerField()
    video_category_id = models.IntegerField()
    video_subcategory_name = models.CharField(max_length=250)
    status = models.CharField(max_length=1)
    ludate = models.DateTimeField()
    insertdate = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'video_subcategory'


class VideoType(models.Model):
    video_type_id = models.AutoField(primary_key=True)
    video_type_name = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'video_type'


class XrefRecipe(models.Model):
    recipe_id = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    variation_id = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    language_id = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    original_recipe_num = models.CharField(max_length=20, blank=True, null=True)
    xref_recipe_id = models.CharField(max_length=20, blank=True, null=True)
    xref_recipe_num = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    insertdate = models.DateTimeField()
    new_xref_recipe_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'xref_recipe'
