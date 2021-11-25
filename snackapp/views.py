from django.shortcuts import render, redirect
from django.http import JsonResponse ## For Sending Json Responses
from django.views import View ## Allows our class to act as a view
from .helpers import GetBody
from .models import Products, Todo
from django.core.serializers import serialize
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, TokenSerializer, MyTokenObtainPairSerializer
from .serializers import TodoSerializer, ProductsSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# new
from decouple import config
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import jwt
# JWT settings
from rest_framework_simplejwt.tokens import RefreshToken


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
   

class RegisterUsersView(generics.ListCreateAPIView):
    """
    POST user/signup/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username or not password or not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)

class LoginView(generics.ListCreateAPIView):
    """
    POST user/login/
    """

    # This permission class will overide the global permission class setting
    # Permission checks are always run at the very start of the view, before any other code is allowed to proceed.
    # The permission class here is set to AllowAny, which overwrites the global class to allow anyone to have access to login.
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer(data={
                # using DRF JWT utility functions to generate a token
                "token": str(refresh.access_token)
                })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class TodoViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Todo.objects.all()
    # The serializer class for serializing output
    serializer_class = TodoSerializer
    # optional permission class set permission level
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #Coule be [permissions.IsAuthenticated]

#Products
class ProductsViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Products.objects.all()
    # The serializer class for serializing output
    serializer_class = ProductsSerializer
    # optional permission class set permission level
    # permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.AllowAny]

class FirstView(View):
    #since the methods name is "get" it will run on "get" requests
    def get(self, request):
        return JsonResponse({"hello":"world", "method": request.method})

    #since the methods name is "post" it will run on "post" requests
    def post(self, request):
        return JsonResponse({"hello":"world", "method": request.method})

    #since the methods name is "put" it will run on "put" requests
    def put(self, request):
        return JsonResponse({"hello":"world", "method": request.method})

    #since the methods name is "delete" it will run on "delete" requests
    def delete(self, request):
        return JsonResponse({"hello":"world", "method": request.method})


class SecondView(View):
    def get(self, request, param):
        query = request.GET.get("query", "no query") ## Grab query from url query
        return JsonResponse({"param": param, "query": query})

    def post(self, request, param):
        query = request.GET.get("query", "no query")
        return JsonResponse({"param": param, "query": query})

    def put(self, request, param):
        query = request.GET.get("query", "no query")
        return JsonResponse({"param": param, "query": query})

    def delete(self, request, param):
        query = request.GET.get("query", "no query")
        return JsonResponse({"param": param, "query": query})

class ThirdView(View):
    def post(self, request):
        return JsonResponse(GetBody(request))


@api_view(['POST'])
@permission_classes([AllowAny])
def get_tokens_for_user(request):

    username = request.POST.get("username")
    password = request.POST.get("password")
    
    user = authenticate(username=username, password=password);

    if user is not None:

        refreshToken = RefreshToken.for_user(user)
        accessToken = refreshToken.access_token

        decodeJTW = jwt.decode(str(accessToken), config('SECRET_KEY'), algorithms=["HS256"]);

        # add payload here!!
        decodeJTW['iat'] = '1590917498'
        decodeJTW['user'] = username
        decodeJTW['date'] = '2020-05-31'

        #encode
        encoded = jwt.encode(decodeJTW, config('SECRET_KEY'), algorithm="HS256")
    
        return Response({
            'status': True,
            'refresh': str(refreshToken),
            'access': str(encoded),
        })

    else:
        return Response({
            'status': False
        })