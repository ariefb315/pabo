from rest_framework import serializers
from .models import Ms_Pegawai

class PegawaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ms_Pegawai
        fields = '__all__'