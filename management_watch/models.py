from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_admin = models.BooleanField('admin status', default=False)
    is_user = models.BooleanField('user status', default=False)

    def __str__(self):
        return self.username

CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'

class Merek(models.Model):
    nama_merek = models.CharField(max_length=100)
    nama_pendiri = models.CharField(max_length=100)
    tahun_berdiri = models.IntegerField(default=0)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='merek_created')

    def __str__(self):
        return self.nama_merek

class Model(models.Model):
    nama_model = models.CharField(max_length=100)
    nama_pencipta = models.CharField(max_length=100, default="")
    tahun_peluncuran = models.IntegerField(default=0)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='model_created')

    def __str__(self):
        return self.nama_model

class Negara(models.Model):
    nama_negara = models.CharField(max_length=100)
    mata_uang = models.CharField(max_length=100)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='negara_created')

    def __str__(self):
        return self.nama_negara

class Jumlah(models.Model):
    jumlah_jam = models.IntegerField(default=0)
    jumlah_baterai = models.IntegerField(default=0)
    jumlah_tali = models.IntegerField(default=0)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='jumlah_created')

    def __str__(self):
        return f"Jam: {self.jumlah_jam}, Baterai: {self.jumlah_baterai}, Tali: {self.jumlah_tali}"

class Harga(models.Model):
    harga_jam = models.IntegerField(default=0)  
    harga_baterai = models.IntegerField(default=0)  
    harga_tali = models.IntegerField(default=0)  
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='harga_created')

    def __str__(self):
        return f"Jam: {self.harga_jam}, Baterai: {self.harga_baterai}, Tali: {self.harga_tali}"

class ManagementWatch(models.Model):
    keterangan = models.CharField(max_length=100)
    merek = models.ForeignKey(Merek, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    negara = models.ForeignKey(Negara, on_delete=models.CASCADE)
    jumlah = models.ForeignKey(Jumlah, on_delete=models.CASCADE)
    harga = models.ForeignKey(Harga, on_delete=models.CASCADE)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='management_watch_created')

    def __str__(self):
        return f"{self.keterangan} - {self.merek.nama_merek} - {self.model.nama_model} - {self.negara.nama_negara} - {self.jumlah.jumlah_jam} - Rp {self.harga.harga_jam}"
