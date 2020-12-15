from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pegawai/', views.Pegawai_list.as_view(), name="api-pegawai" ),
    path('pegawai/<int:pk>', views.Pegawai_detail.as_view(), name='api-pegawai-id'),
]

