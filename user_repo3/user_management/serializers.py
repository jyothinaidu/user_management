from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
# from firebase_admin import auth
from django.contrib.auth import authenticate, user_logged_in
import requests
import json
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler
import pyrebase
import datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import AbstractUser
from firebase import firebase as post_firebase
from rest_framework.validators import UniqueValidator
import base64
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from base import utils as base_utils
from .models import UserProfile,UserAnswers
# from teams.models import TeamInvitation
# from teams.api.serializers import TeamSerializer
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.decorators import api_view,renderer_classes
from django.views.decorators.csrf import csrf_protect
User = get_user_model()


config = {
    "apiKey": "AIzaSyAocN5elkKo42vi7C6svQriwfCufffW_JY",
    "authDomain": "kraft-demo.firebaseapp.com",
    "databaseURL": "https://kraft-demo.firebaseio.com",
    "projectId": "kraft-demo",
    "storageBucket": "kraft-demo.appspot.com",
    "messagingSenderId": "666048778215"
  }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = post_firebase.FirebaseApplication('https://kraft-demo.firebaseio.com/')
import json






class UserLoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=False,
        allow_blank=True,
        write_only=True,
    )

    email = serializers.EmailField(
        required=False,
        allow_blank=True,
        write_only=True,
        label="Email Address"
    )

    token = serializers.CharField(
        allow_blank=True,
        read_only=True
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta(object):
        model = User
        fields = ['email', 'username', 'password', 'token']

    # @api_view(('POST'))
    # @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    # @csrf_protect
    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password', None)

        if not email and not username:
            raise serializers.ValidationError("Please enter username or email to login.")

        user = User.objects.filter(
            Q(email=email) | Q(username=username)
        ).exclude(
            email__isnull=True
        ).exclude(
            email__iexact=''
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Invalid credentials.")

        if user_obj.is_active:
            token, created = Token.objects.get_or_create(user=user_obj)
            data['token'] = token
        else:
            raise serializers.ValidationError("User not active.")
        print ("****************************",data)
        return data

























    # def create(self, validated_data):
    #     data_to_pop = validated_data.pop('favourites')
    #     # for item in data:
    #     fav_id = data_to_pop.__dict__['id']
    #     data = validated_data
    #     data['favourites']=fav_id
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.", data)
    #     fav_obj = Favourites.objects.get(id=fav_id)
    #     firebase_post_preferences = db.post("/preferences",data)
    #
    #     preferences = Preferences.objects.create(favourites = fav_obj,\
    #                                              preferences_name=data['preferences_name'],description = data['description'])
    #
    #     print ("%%%%%%%%%%%%%%%%%%555",preferences)
    #     return firebase_post_preferences

    # def update(self, instance, validated_data):
    #     instance.__dict__.update(validated_data)
    #     instance.save()
    #     return instance




class UserAdminLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=UserProfile.objects.all())]
            )
    password = serializers.CharField(min_length=8)


    def post(self, request):
        email = request.POST.get('email')
        passw = request.POST.get("password")

    class Meta:
        model = UserProfile
        fields = ('id',  'email', 'password')





class UserSerializer(serializers.ModelSerializer):
    preferences_value = serializers.RelatedField(source='preferences',read_only=True,required=False)


    # is called if we save serializer if it do not have amanyn instance
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'first_name', 'preferences_value','last_name', \
                  'phone1', 'gender', 'address', 'password', 'email', 'dob')
        lookup_field  ="id"
        # fields = "__all__"


    def create(self, validated_data):
        data = validated_data
        if data["dob"]!=None:
            a = data["dob"]
            stra = a.strftime('%Y-%m-%d')
            data["dob"]=str(stra)
            db.post("/users",data)
        else:
            data = validated_data
            db.post("/users", data)
        password = validated_data.pop("password")
        user = UserProfile.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    # is called if we save serializer if it have an instance
    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        instance.__dict__.update(validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token


# class PreferencesSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         depth = 1
#         model = Preferences
#         fields = ('id', 'name', 'description')






    # def create(self, validated_data):
    #     data = validated_data
    #     firebase_post_favourites= db.post("/favourites",data)
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.",data)
    #     preferences = Favourites.objects.create(**validated_data)
    #     # preferences.preferences_name=data['preferences_name']
    #     # preferences.description=data['description']
    #     # preferences.favourites='Pizza'
    #     # preferences.save()
    #     # print ("Hello Preferences")
    #     return firebase_post_favourites
    #
    # def update(self, instance, validated_data):
    #     instance.__dict__.update(validated_data)
    #     instance.save()
    #     return instance

























class UserAnswersSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    answer_activity_id = serializers.IntegerField(required=False)
    answer_group_id = serializers.IntegerField(required=False)
    answer_id = serializers.IntegerField(required=False)
    answer_source = serializers.CharField(required=True)
    answer_value = serializers.IntegerField(required=False)
    choce_id = serializers.IntegerField(required=False)
    language_id = serializers.IntegerField(required=False)
    question_id = serializers.IntegerField(required=False)
    status = serializers.IntegerField(required=False)
    weight_value = serializers.IntegerField(required=False)

    class Meta(object):
        model = UserAnswers
        fields = '__all__'

    def create(self, validated_data):
        return UserAnswers.objects.create(**validated_data)


class UserPreferenceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    preferences_name = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=500)
    favourites = serializers.PrimaryKeyRelatedField(queryset=Favourites.objects.all())

    class Meta:
        model = Preferences
        fields = ( 'id','preferences_name', 'description','favourites')
        # lookup_field  ="id"
        # fields = "__all__"

    # def create(self, validated_data):
    #     data = validated_data.pop('favourites').__dict__
    #     final_data =validated_data
    #     final_data['favourites'] =  data['name']
    #     print (":::::::?????????",final_data)
    #
    #     return Preferences.objects.create(**final_data)



class FavouritesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    class Meta:
        model = Favourites
        fields = "__all__"

    def create(self, validated_data):
        return Favourites.objects.create(**validated_data)




class UserRegistrationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    email = serializers.EmailField(required=True,label="Email Address")

    password = serializers.CharField(required=True,label="Password",style={'input_type': 'password'})

    password_2 = serializers.CharField(required=True,label="Confirm Password",style={'input_type': 'password'})

    first_name = serializers.CharField(required=True)

    last_name = serializers.CharField(required=True)

    site_id = serializers.IntegerField(required=False)

    is_active = serializers.BooleanField(default=True)

    is_staff = serializers.BooleanField(default=True)

    dob = serializers.DateField(input_formats=None)
    phone1 = serializers.IntegerField(required=False)
    phone2 = serializers.IntegerField(required=False)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES,required=False)
    address1 = serializers.CharField(required=True)
    address2 = serializers.CharField(required=True)
    registration_activity_id = serializers.CharField(required=True)
    registration_source = serializers.ChoiceField(choices=REGISTRATION_SOURCES,required=False)
    language_id = serializers.CharField(required=True)
    nickname = serializers.CharField(required=True)
    news_letter = serializers.BooleanField(default=True)
    # answers = serializers.StringRelatedField(many=True)
    answers = serializers.PrimaryKeyRelatedField(queryset=UserAnswers.objects.all())
    favourites = serializers.PrimaryKeyRelatedField(queryset=Favourites.objects.all())
    preferences = serializers.PrimaryKeyRelatedField(queryset=Preferences.objects.all())


    class Meta(object):
        model = User
        fields = ['id','username', 'email', 'password', 'password_2', 'first_name', 'last_name', 'site_id',
                  'news_letter','nickname','language_id','registration_source','registration_activity_id',
                  'address2','address1','gender','phone2','phone1','dob','is_staff','is_active','answers',
                  'preferences','favourites']
        # fields = '__all__'
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
            raise serializers.ValidationError(
                "Password should be atleast %s characters long." % getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
            )
        return value

    def validate_password_2(self, value):
        data = self.get_initial()
        password = data.get('password')
        if password != value:
            raise serializers.ValidationError("Passwords doesn't match.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    # def validate_invite_code(self, value):
    #     data = self.get_initial()
    #     email = data.get('email')
    #     if value:
    #         self.invitation = TeamInvitation.objects.validate_code(email, value)
    #         if not self.invitation:
    #             raise serializers.ValidationError("Invite code is not valid / expired.")
    #         self.team = self.invitation.invited_by.team.last()
    #     return value

    def create(self, validated_data):

        user_data = {
            'username': validated_data.get('username'),
            'email': validated_data.get('email'),
            'password': validated_data.get('password'),
            'first_name': validated_data.get('first_name'),
            'last_name': validated_data.get('last_name')
        }

        user = UserProfile.objects.create_user_profile(
                data=user_data,
                # is_active=is_active,
                site=get_current_site(self.context['request']),
                send_email=True
            )

        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=False,
        allow_blank=True,
        write_only=True,
    )

    email = serializers.EmailField(
        required=False,
        allow_blank=True,
        write_only=True,
        label="Email Address"
    )

    token = serializers.CharField(
        allow_blank=True,
        read_only=True
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta(object):
        model = User
        fields = ['email', 'username', 'password', 'token']

    # @api_view(('POST'))
    # @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    @csrf_protect
    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password', None)

        if not email and not username:
            raise serializers.ValidationError("Please enter username or email to login.")

        user = User.objects.filter(
            Q(email=email) | Q(username=username)
        ).exclude(
            email__isnull=True
        ).exclude(
            email__iexact=''
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Invalid credentials.")

        if user_obj.is_active:
            token, created = Token.objects.get_or_create(user=user_obj)
            data['token'] = token
        else:
            raise serializers.ValidationError("User not active.")
        print ("****************************",data)
        return serializers.ValidationError(data)


class PasswordResetSerializer(serializers.Serializer):

    email = serializers.EmailField(
        required=True
    )

    def validate_email(self, value):
        # Not validating email to have data privacy.
        # Otherwise, one can check if an email is already existing in database.
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):

    token_generator = default_token_generator

    def __init__(self, *args, **kwargs):
        context = kwargs['context']
        uidb64, token = context.get('uidb64'), context.get('token')
        if uidb64 and token:
            uid = base_utils.base36decode(uidb64)
            self.user = self.get_user(uid)
            self.valid_attempt = self.token_generator.check_token(self.user, token)
        super(PasswordResetConfirmSerializer, self).__init__(*args, **kwargs)

    def get_user(self, uid):
        try:
            user = User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return user

    new_password = serializers.CharField(
        style={'input_type': 'password'},
        label="New Password",
        write_only=True
    )

    new_password_2 = serializers.CharField(
        style={'input_type': 'password'},
        label="Confirm New Password",
        write_only=True
    )

    def validate_new_password_2(self, value):
        data = self.get_initial()
        new_password = data.get('new_password')
        if new_password != value:
            raise serializers.ValidationError("Passwords doesn't match.")
        return value

    def validate(self, data):
        if not self.valid_attempt:
            raise serializers.ValidationError("Operation not allowed.")
        return data


class UserSerializer(serializers.ModelSerializer):

    # team = TeamSerializer(many=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'has_email_verified']