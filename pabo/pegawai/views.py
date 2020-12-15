from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
# Create your views here.
from .models import Ms_Pegawai
from .serializers import PegawaiSerializer

from django.contrib.auth.views import LoginView
from django.urls import reverse

# import coreapi

def index(request):
    return redirect('api-pegawai')
    
class Pegawai_list(generics.ListCreateAPIView):
    queryset = Ms_Pegawai.objects.all()
    serializer_class = PegawaiSerializer
    name="Daftar Pegawai"
    # permission_classes = (permissions.IsAuthenticated,)
    
class Pegawai_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ms_Pegawai.objects.all()
    serializer_class = PegawaiSerializer
    name="Daftar Pegawai Detail"
    # permission_classes = (permissions.IsAuthenticated,)

class MyLoginView():

    def get_success_url(self):
        url = self.get_redirect_url
        return url or reverse('api-pegawai')

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter