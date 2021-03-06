# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 18:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_activity_id', models.IntegerField()),
                ('answer_group_id', models.IntegerField()),
                ('answer_id', models.IntegerField()),
                ('answer_source', models.CharField(blank=True, max_length=200, null=True)),
                ('answer_value', models.IntegerField()),
                ('choce_id', models.IntegerField()),
                ('language_id', models.IntegerField()),
                ('question_id', models.IntegerField()),
                ('status', models.IntegerField()),
                ('weight_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_updated', models.DateTimeField(auto_now=True)),
                ('has_email_verified', models.BooleanField(default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('site_id', models.IntegerField(default=1)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('dob', models.DateField(null=True)),
                ('phone1', models.IntegerField(blank=True, null=True)),
                ('phone2', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6)),
                ('address1', models.CharField(blank=True, max_length=500, null=True)),
                ('address2', models.CharField(blank=True, max_length=500, null=True)),
                ('password', models.CharField(max_length=255)),
                ('registration_activity_id', models.CharField(max_length=200)),
                ('registration_source', models.CharField(choices=[('Google', 'Google'), ('Facebook', 'Facebook'), ('Github', 'Github'), ('Other', 'Other')], max_length=100)),
                ('language_id', models.CharField(db_index=True, max_length=20)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('news_letter', models.BooleanField(default=True)),
                ('verification_key', models.CharField(max_length=40)),
                ('answers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.UserAnswers')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'user profiles',
                'verbose_name': 'user profile',
            },
        ),
    ]
