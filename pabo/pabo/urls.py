"""pabo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, path
from django.conf.urls import url
from allauth.account import views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from pegawai.views import GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pegawai.urls')),

    #kebutuhan dokumentasi
    path('openapi', get_schema_view(
        title="Sistem Kepegawaian",
        description="API untuk melakukan share data kepegawaian",
        # url="http://localhost:8000",
        version="1.0.0"
    ), name="openapi-schema"),
    path('swagger-ui/', TemplateView.as_view(
        template_name="swagger-ui.html",
    ), name="swagger-ui"),
    
    #kebutuhan auth
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('accounts/', include('allauth.urls')),
    path('api-auth/login/', views.login, name='account_login'),
    path('api-auth/logout/', views.logout, name='account_logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    
]
