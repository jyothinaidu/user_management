from .serializers1 import AssetsSerialzer, RecipesSerializer, PictureFormatSerializer
from .modes1 import Assets, Recipes, PictureFormats
from rest_framework import viewsets


class AssetsView(viewsets.ModelViewSet):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerialzer


class RecipesView(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer


class PicturesView(viewsets.ModelViewSet):
    queryset = PictureFormats.objects.all()
    serializer_class = PictureFormatSerializer


# class RegistrationView(APIView):
#     permission_classes = ()
#
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.DATA)
#
#     # Check format and unique constraint
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         data = serializer.data
#         u = User.objects.create(username=data['username'])
#         u.set_password(data['password'])
#         u.save()
#
#         # Create OAuth2 client
#         name = u.username
#         client = Client(user=u, name=name, url='' + name, client_id=name, client_secret='', client_type=1)
#         client.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)