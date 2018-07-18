from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)
from rest_framework.renderers import TemplateHTMLRenderer
from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth
from firebase_admin import db
import os
from .serializers import UserLoginSerializer
import firebase
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cred = credentials.Certificate(os.path.join(BASE_DIR, 'ADMIN_CREDENTIALS.json'))
# default_app = firebase.FirebaseApplication('https://kraft-fd9cf.firebaseio.com/')
from .user_management_api import default_app
import pyrebase
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from .serializers import  UserSerializer
from rest_framework import generics
from .serializers import  UserSerializer
from rest_framework import generics
from .serializers import  UserSerializer,UserAdminLoginSerializer
from rest_framework import generics
from .serializers import  UserSerializer
from rest_framework import mixins
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from firebase_admin import auth
from rest_framework.renderers import TemplateHTMLRenderer
from . import serializers
from . import views
config = {
    "apiKey": "AIzaSyAocN5elkKo42vi7C6svQriwfCufffW_JY",
    "authDomain": "kraft-demo.firebaseapp.com",
    "databaseURL": "https://kraft-demo.firebaseio.com",
    "projectId": "kraft-demo",
    "storageBucket": "kraft-demo.appspot.com",
    "messagingSenderId": "666048778215"
  }
from django.contrib.sites.shortcuts import get_current_site
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database=firebase.database()
from firebase import firebase as post_firebase
db = post_firebase.FirebaseApplication('https://kraft-demo.firebaseio.com/')

from django.core.exceptions import ValidationError








def home(request):
    return render(request, 'accounts/login.html')

def index(request):
    return render(request, 'accounts/index.html')








class UserPreferenceAPIView(generics.CreateAPIView):
    """
    Endpoint for user registration.

    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.UserPreferenceSerializer
    queryset = Preferences.objects.all()


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class PreferencesFavouriteCreateView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.FavouritesSerializer
    queryset = Favourites.objects.all()




class UserAnswersCreateView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserAnswersSerializer
    queryset = UserAnswers.objects.all()





class UserRegistrationAPIView(generics.CreateAPIView):
    """
    Endpoint for user registration.

    """
    # renderer_classes = [TemplateHTMLRenderer]

    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.UserRegistrationSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserEmailVerificationAPIView(views.APIView):
    """
    Endpoint for verifying email address.

    """

    permission_classes = (permissions.AllowAny, )

    def get(self, request, verification_key):
        activated_user = self.activate(verification_key)
        if activated_user:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def activate(self, verification_key):
        return UserProfile.objects.activate_user(verification_key)


class UserLoginAPIView(views.APIView):
    """
    Endpoint for user login. Returns authentication token on success.

    """
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'accounts/login.html'
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.UserLoginSerializer

    # @csrf_protect
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ",serializer.is_valid())
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetAPIView(views.APIView):
    """
    Endpoint to send email to user with password reset link.

    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.PasswordResetSerializer

    def post(self, request):
        user_profile = self.get_user_profile(request.data.get('email'))
        if user_profile:
            user_profile.send_password_reset_email(
                site=get_current_site(request)
            )  # To be made asynchronous in production
            return Response(status=status.HTTP_200_OK)

        # Forcing Http status to 200 even if failure to support user privacy.
        # Will show message at frontend like "If the email is valid, you must have received password reset email"
        return Response(status=status.HTTP_200_OK)

    def get_user_profile(self, email):
        try:
            user_profile = UserProfile.objects.get(user__email=email)
        except:
            return None
        return user_profile


class PasswordResetConfirmView(views.APIView):
    """
    Endpoint to change user password.

    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.PasswordResetConfirmSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            data=request.data,
            context={
                'uidb64': kwargs['uidb64'],
                'token': kwargs['token']
            })

        if serializer.is_valid(raise_exception=True):
            new_password = serializer.validated_data.get('new_password')
            user = serializer.user
            user.set_password(new_password)
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(generics.RetrieveAPIView):
    """
    Endpoint to retrieve user profile.

    """

    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.UserProfileSerializer

    def get_object(self):
        return self.request.user.userprofile


























class AdminLoginView(generics.CreateAPIView):
    serializer_class = UserAdminLoginSerializer

    def post(self, request):
        email = request.POST.get('email')
        passw = request.POST.get("password")
        try:
            user = authe.sign_in_with_email_and_password(email, passw)
            if user:
                return Response(user,status=status.HTTP_200_OK)
        except:
            message = "invalid credentials"
        return Response(message, status=status.HTTP_200_OK)
class AdminLogoutView(APIView):



    def get(self,request):
        logout(request)
        message = "User is Logged Out"
        return Response(message, status=status.HTTP_200_OK)
        # raise ValidationError(message)






#
#
#
#
# class PreferencesCreateView(generics.CreateAPIView):
#     serializer_class = UserPreferenceSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = UserPreferenceSerializer(data=request.data)
#         print(serializer)
#         data = request.data
#         firebase_post_preferences = db.post("/preferences", data)
#         if serializer.is_valid():
#             instance = serializer.save()
#             headers = self.get_success_headers(serializer.data)
#             serializer = UserPreferenceSerializer(instance)
#             return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class PreferencesListView(generics.ListAPIView):
#     queryset = Preferences.objects.all()
#     serializer_class = UserPreferenceSerializer
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         preferences = database.child("/preferences").get().val()
#         return Response(preferences)
#
#
# class PreferencesDetailView(generics.RetrieveAPIView):
#     queryset = Preferences.objects.all()
#     serializer_class = UserPreferenceSerializer
#
#     def user_details(self,request, pk):
#         preferences = database.child("/preferences").get().val()
#         return Response(preferences)
#
# class PreferencesUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = Preferences.objects.all()
#     serializer_class = UserPreferenceSerializer
#
#
#
#
# class PreferencesFavouriteCreateView(generics.CreateAPIView):
#     queryset = Favourites.objects.all()
#     serializer_class = FavouritesSerializer
#
#     # def get_object(self, id):
#     #     try:
#     #         return Favourites.objects.get(id=id)
#     #     except Favourites.DoesNotExist:
#     #         raise Http404
#
#
# class PreferencesFavouriteListApiView(generics.ListAPIView):
#     queryset = Favourites.objects.all()
#     serializer_class = FavouritesSerializer
#
#
#






class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UsersListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users_list.html'

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = database.child("/users").get().val()
        return Response(usernames)





class UserDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def user_details(self,request, pk):
        usernames = database.child("/users").get().val()
        return Response(usernames)


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer




class UserDeleteView(generics.DestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def delete_user(request, id):
        user = get_object_or_404(UserProfile, id=id)
        user.delete()
        return Response({"message": "Deleted"})




class LogoutView(APIView):

    """

    Calls Django logout method and delete the Token object

    assigned to the current User object.



    Accepts/Returns nothing.

    """

    permission_classes = (AllowAny,)



    def get(self, request, *args, **kwargs):

        if getattr(settings, 'ACCOUNT_LOGOUT_ON_GET', False):

            response = self.logout(request)

        else:

            response = self.http_method_not_allowed(request, *args, **kwargs)



        return self.finalize_response(request, response, *args, **kwargs)



    def post(self, request, *args, **kwargs):

        return self.logout(request)



    def logout(self, request):

        try:

            request.user.auth_token.delete()

        except (AttributeError, ObjectDoesNotExist):

            pass



        django_logout(request)



        return Response({"detail": _("Successfully logged out.")},

                        status=status.HTTP_200_OK)
class LoginView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        # profile = get_object_or_404(Users,user_id=1)
        # serializer = UserSerializer(profile)
        return Response({})

class LogoutView(LogoutView):
    authentication_classes = (authentication.TokenAuthentication,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'


class TestAuthView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request, format=None):
        return Response(data=request.data,template_name='home.html')







class UserLoginAPIView(APIView):
    """
    Endpoint for user login. Returns authentication token on success.

    """
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'accounts/login.html'
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserLoginSerializer
    #
    # @csrf_protect
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

