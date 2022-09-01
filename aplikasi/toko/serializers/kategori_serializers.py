from rest_framework import serializers

from aplikasi.toko.models import Kategori

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

