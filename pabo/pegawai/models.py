from django.db import models

class Ms_Pegawai(models.Model):
    nip = models.CharField(max_length=30)
    nama = models.CharField(max_length=75)
    pangkat = models.CharField(max_length=50)
    gol = models.CharField(max_length=10)
    unit_kerja = models.CharField(max_length=30)

    def __str__():
        return self.nama
