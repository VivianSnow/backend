from django.shortcuts import render
from .serializers import LoginSerializer
from rest_framework.authtoken.views import ObtainAuthToken

# Create your views here.

class MyObtainAuthToken(ObtainAuthToken):
    """
    Login Auth
    In order to return specific code, we rewrite TokenSerializer class
    """
    serializer_class = LoginSerializer