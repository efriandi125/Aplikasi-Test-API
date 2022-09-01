import uuid
from django.db import models

# Create your models here.
class Customer(models.Model):
    id_customer= models.UUIDField(primary_key=True, default=uuid.uuid4)
    nama = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

class Produk(models.Model):
    id_Produk = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nama_Produk = models.CharField(max_length=40)
    harga = models.IntegerField()
    qty = models. IntegerField()
    kategoris = models.ForeignKey('Kategori', on_delete=models.CASCADE,blank=True)

class Transaksi(models.Model):
    id_transaksi = models.UUIDField(primary_key=True, default=uuid.uuid4)
    #produks = models.ForeignKey('Produk',on_delete=models.CASCADE,null=True,blank=True)
    qty_trans = models.IntegerField()
    total = models.IntegerField()
    customers = models.ForeignKey('Customer', on_delete=models.CASCADE,blank=True)
    carts= models.ForeignKey('Keranjang',on_delete=models.CASCADE,blank=True)
class Kategori(models.Model):
    id_kategori = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nama_kategori = models.CharField(max_length=40)

class Keranjang(models.Model):
    id_cart = models.UUIDField(primary_key=True, default=uuid.uuid4)
    status= models.BooleanField(null=True,blank=True)
    total_cart = models.IntegerField()
    customers = models.ForeignKey('Customer', on_delete=models.CASCADE,blank=True)

class KeranjangDetail(models.Model):
    id_keranjang_detail = models.UUIDField(primary_key=True,default=uuid.uuid4)
    products = models.ForeignKey('Produk',on_delete=models.CASCADE,blank=True)
    qty_cart =models.IntegerField()
    total_harga= models.IntegerField()
    carts= models.ForeignKey('Keranjang',on_delete=models.CASCADE,blank=True)

    class Meta:
        db_table ='toko_apps'
