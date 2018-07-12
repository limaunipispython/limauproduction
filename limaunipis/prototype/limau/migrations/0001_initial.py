# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 06:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(default='description of announcement', max_length=50)),
                ('text', models.TextField(default='write the announcement here')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_bm', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='article_thumbnail')),
                ('text_bm', models.TextField()),
                ('slug', models.SlugField(default='will-be-generated-once-save')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bm', models.CharField(max_length=128)),
                ('name_en', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('slug', models.SlugField(default='will-be-generated-once-save')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bm', models.CharField(max_length=128)),
                ('name_en', models.CharField(max_length=128)),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='ingredient_thumbnail')),
                ('description', models.TextField()),
                ('slug', models.SlugField(default='will-be-generated-once-save')),
            ],
        ),
        migrations.CreateModel(
            name='MobileBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='description', max_length=100)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='mobilebanner')),
                ('status', models.IntegerField(choices=[[1, 'active'], [2, 'nonactive']], default=2)),
                ('image_url', models.URLField(default='www.google.com')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='fill in your product name here', max_length=100)),
                ('image_1', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='products')),
                ('image_2', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='products')),
                ('image_3', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='products')),
                ('image_4', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='products')),
                ('definition', models.CharField(default='Fill in product short definition here', max_length=300)),
                ('optional_definition_switch', models.BooleanField(default=True)),
                ('optional_definition', models.TextField(default='Fill in extra definition in HTML form here if switch = true')),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_switch', models.BooleanField(default=False)),
                ('discount', models.DecimalField(decimal_places=2, default='5.00', max_digits=10)),
                ('in_stock', models.BooleanField(default=True)),
                ('discounted_price', models.DecimalField(decimal_places=2, default='50.00', max_digits=10)),
                ('member_price_switch', models.BooleanField(default=False)),
                ('discount_member', models.DecimalField(decimal_places=2, default='7.50', max_digits=10)),
                ('discounted_member_price', models.DecimalField(decimal_places=2, default='50.00', max_digits=10)),
                ('slug', models.SlugField(default='will-be-generated-once-save')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProductBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='productBanners')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(default='fill in product description here')),
                ('slug', models.SlugField(default='will-be-generated-once-save')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bm', models.CharField(max_length=128)),
                ('name_en', models.CharField(max_length=128)),
                ('youtube_url', models.URLField()),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='recipe_thumbnail')),
                ('thumbnail2', imagekit.models.fields.ProcessedImageField(upload_to='recipe_thumbnail')),
                ('thumbnail3', imagekit.models.fields.ProcessedImageField(upload_to='recipe_thumbnail')),
                ('description', models.TextField(default='type a description of your recipe')),
                ('ingredient_content', models.TextField(default='type your ingredients here, in <li> form')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(default='will-be-generated-once-save')),
                ('serve', models.IntegerField(choices=[[1, 'ONE'], [2, 'TWO'], [3, 'THREE'], [4, 'FOUR'], [5, 'FIVE'], [6, 'SIX'], [6, 'SEVEN'], [6, 'EIGHT'], [6, 'NINE'], [6, 'TEN']], default=3)),
                ('instruction', models.TextField(default='fill in step by step instruction here')),
                ('ingredients', models.ManyToManyField(to='limau.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bm', models.CharField(max_length=128)),
                ('name_en', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('slug', models.SlugField(default='will-be-generated-once-save')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bm', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('building_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='restaurant_thumbnail/building')),
                ('menu_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='restaurant_thumbnail/menu')),
                ('food_thumbnail_1', imagekit.models.fields.ProcessedImageField(upload_to='restaurant_thumbnail/food')),
                ('food_thumbnail_2', imagekit.models.fields.ProcessedImageField(upload_to='restaurant_thumbnail/food')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('food_quality', models.IntegerField(choices=[[1, 'ONE'], [2, 'TWO'], [3, 'THREE'], [4, 'FOUR'], [5, 'FIVE']], default=1)),
                ('food_variety', models.IntegerField(choices=[[1, 'ONE'], [2, 'TWO'], [3, 'THREE'], [4, 'FOUR'], [5, 'FIVE']], default=1)),
                ('etiquette', models.IntegerField(choices=[[1, 'ONE'], [2, 'TWO'], [3, 'THREE'], [4, 'FOUR'], [5, 'FIVE']], default=1)),
                ('cleanliness', models.IntegerField(choices=[[1, 'ONE'], [2, 'TWO'], [3, 'THREE'], [4, 'FOUR'], [5, 'FIVE']], default=1)),
                ('access', models.IntegerField(choices=[[1, 'ONE'], [2, 'TWO'], [3, 'THREE'], [4, 'FOUR'], [5, 'FIVE']], default=1)),
                ('limau_meter', models.IntegerField(default=1)),
                ('starhtml', models.TextField(default='nothing')),
                ('slug', models.SlugField(default='will-be-generated-once-save')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bm', models.CharField(max_length=128)),
                ('name_en', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('slug', models.SlugField(default='will-be-generated-once-save')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', imagekit.models.fields.ProcessedImageField(blank=True, default='/media/user_picture/Koala.jpg', null=True, upload_to='user_picture')),
                ('description', models.TextField(default='description', max_length=300)),
                ('badge', models.IntegerField(choices=[[1, 'gold'], [2, 'silver'], [3, 'bronze']], default=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bm', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(default='my food is the best in the world!!', max_length=300)),
                ('ingredients', models.TextField(default='key in your ingredienst here in <li>ingredients</li> tag')),
                ('instructions', models.TextField(default='key in your instruction here in <li>ingredients<li> tag')),
                ('picture_1', imagekit.models.fields.ProcessedImageField(upload_to='user_recipe_thumbnail')),
                ('picture_2', imagekit.models.fields.ProcessedImageField(upload_to='user_recipe_thumbnail')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(default='will-be-generated-once-save')),
                ('recipecategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='limau.RecipeCategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='restaurantcategory',
            field=models.ManyToManyField(to='limau.RestaurantCategory'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipecategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='limau.RecipeCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='limau.ProductCategory'),
        ),
        migrations.AddField(
            model_name='article',
            name='articlecategory',
            field=models.ManyToManyField(to='limau.ArticleCategory'),
        ),
    ]