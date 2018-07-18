
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from django.http import Http404
import os
# from firebase_admin import credentials, auth
# import firebase_admin
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render
import pyrebase
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import firebase_admin
from firebase_admin import auth
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials
from django.contrib.auth.views import LogoutView, LoginView
from .authentication import ExampleAuthentication,SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.views import ObtainJSONWebToken
import datetime
# from .serializers import JWTSerializer
from firebase_admin import db
from rest_framework_simplejwt.views import TokenObtainPairView
from firebase import firebase
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cred = credentials.Certificate(os.path.join(BASE_DIR, 'ADMIN_CREDENTIALS.json'))
default_app = firebase.FirebaseApplication('https://kraft-fd9cf.firebaseio.com/')
from .permissions import (
    IsOwnerOrReadOnly, IsAdminUserOrReadOnly, IsSameUserAllowEditionOrReadOnly
)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,UserAdminLoginSerializer
from .models import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template.loader import get_template
from rest_framework.renderers import StaticHTMLRenderer

config = {
    "apiKey": "AIzaSyAocN5elkKo42vi7C6svQriwfCufffW_JY",
    "authDomain": "kraft-demo.firebaseapp.com",
    "databaseURL": "https://kraft-demo.firebaseio.com",
    "projectId": "kraft-demo",
    "storageBucket": "kraft-demo.appspot.com",
    "messagingSenderId": "666048778215"
  }




firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database=firebase.database()

@api_view(('GET','POST'))
@renderer_classes((StaticHTMLRenderer,))
def api_root(request, format=None):
    final_output = {
        # 'Admin Login Method': reverse('login_fire_base', request=request, format=format),
        'Users List': reverse('users_list', request=request, format=format),
        'Swagger Documentation': reverse('swagger-details', request=request, format=format),
        'User Login': reverse('admin_firebase_auth', request=request, format=format),
        'User Logout': reverse('admin_firebase_logout', request=request, format=format),
        'Create user': reverse('user_create', request=request, format=format),
        # 'Update user': reverse('user_update', request=request, format=format),
        'Delete user': reverse('user_delete', request=request, format=format),


        # 'Preferences user': reverse('preferences_list', request=request, format=format),
        # 'Preferences Create': reverse('preferences_create', request=request, format=format),
        # 'Favourites Create': reverse('favourites_create', request=request, format=format),
        # 'Favourites List': reverse('favourites_list', request=request, format=format),


        # 'Preferences List': reverse('user_preferences', request=request, format=format),
        # 'Preferences Favorites': reverse('user_preferences_favourites', request=request, format=format),
        #
        # 'Assets List': reverse('Assets-List', request=request, format=format),
        # # 'Assets-Detail':reverse('Assets-Detail', request=request, format=format),
        # 'Categories-List': reverse('Categories-List', request=request, format=format),
        # # 'Categories-Detail': reverse('Categories-Detail', request=request, format=format),
        # 'Dishes-List': reverse('Dishes-List', request=request, format=format),
        # # 'Dishes-Detail': reverse('Dishes-Detail', request=request, format=format),
        # 'Ingredients-List': reverse('Ingredients-List', request=request, format=format),
        # # 'Ingredients-detail': reverse('Ingredients-detail', request=request, format=format),
        # 'RiseIngredients-list': reverse('RiseIngredients-list', request=request, format=format),
        # # 'RiseIngredients-detail': reverse('RiseIngredients-detail', request=request, format=format),
        # 'Taxonomy-List': reverse('Taxonomy-List', request=request, format=format),
        # # 'Taxonomy-detail':reverse('Taxonomy-detail', request=request, format=format),
        # 'Recipes-List': reverse('Recipes-List', request=request, format=format),
        # # 'Recipes-Detail': reverse('Recipes-Detail', request=request, format=format),
        # 'Recipes-meal_plan-List': reverse('Recipes-meal_plan-List', request=request, format=format),
        # # 'Recipes-meal_plan-Detail': reverse('Recipes-meal_plan-Detail', request=request, format=format),
        # 'Meal_Plan-List': reverse('Meal_Plan-List', request=request, format=format),
        # # 'Meal_Plan-Detail': reverse('Meal_Plan-Detail', request=request, format=format),



    }

    # t = get_template('login.html')
    # html = t.render(final_output)
    return render(request,'tables.html',{'final_output':final_output})


@api_view(['GET'])
def user_api_root(request, format=None):
    data = {
    'Users List': reverse('users_list', request=request, format=format),
    'Swagger Documentation': reverse('swagger-details', request=request, format=format),
    'User Login': reverse('admin_firebase_auth', request=request, format=format),
    'User Logout': reverse('admin_firebase_logout', request=request, format=format),
    'Create user': reverse('user_create', request=request, format=format),
    # 'Update user': reverse('user_update', request=request, format=format),
    'Delete user': reverse('user_delete', request=request, format=format),
    'Preferences user': reverse('preferences_list', request=request, format=format),
    'Preferences Create': reverse('preferences_create', request=request, format=format),
    'Favourites Create': reverse('favourites_create', request=request, format=format),
    'Favourites List': reverse('favourites_list', request=request, format=format),
    }
    return render(request, 'users_api.html', {'data':data})

def login(request,format=None):

    return render(request, 'login.html')
    # pass
#     if request.method == 'GET':
#         return render(request, "login.html")
#     else:
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         user = auth.authenticate(username=username, password=password)
#
#         if not user:
#             return render_json({'ret_code': 1})
#
#         auth.login(request, user)
#         return render_json({'ret_code': 0})



class AdminAuthView(APIView):
    authentication_classes = (SessionAuthentication, ExampleAuthentication,)
    permission_classes = (IsAuthenticated,)


    def post(self, request, format=None):
        content = {
            'user': request.user,
            'auth': request.auth,  # None
        }
        return Response(content)


class UserListApiView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)

    def profile(self, request):
        u = UserProfile.objects.filter(pk=request.user.pk)[0]
        p = Preferences.objects.filter(user=u)[0]
        return Response({"id": u.id, "first_name": u.first_name, "last_name": u.last_name, "email": u.email,
                         "city": p.description, "country": p.name})



@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created"})
    else:
        data = {
          "error": True,
          "errors": serializer.errors,
        }
        return Response(data)





@api_view(["GET"])
def user_details(request, pk):
    user = UserProfile.objects.get(id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)



@api_view(["GET", "PUT"])
def user_update(request, pk):
    user = UserProfile.objects.get(id=pk)
    if request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": serializer.errors, "error": True})
    serializer = UserSerializer(user)
    return Response(serializer.data)



@api_view(["GET"])
def users_list(request):
    users = UserProfile.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)





def delete_user(request, pk):
    user = get_object_or_404(User, id=pk)
    user.delete()
    return Response({"message": "Deleted"})













