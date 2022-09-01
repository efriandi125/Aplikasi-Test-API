from rest_framework import serializers

from aplikasi.toko.models import Kategori, Produk
from aplikasi.toko.serializers.kategori_serializers import KategoriSerializer


class ProdukSerializer(serializers.ModelSerializer):
    kategoris= KategoriSerializer(write_only=True)
    class Meta:
        model = Produk
        fields = '__all__'
    
    def create(self,validated_data):
        val= validated_data.pop('kategoris')
        kategoris= Kategori.objects.create(**val)
        prd=Produk.objects.create(kategoris=kategoris,**validated_data)
        return prd