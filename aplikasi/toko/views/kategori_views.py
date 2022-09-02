from rest_framework import viewsets
from aplikasi.toko.models import Kategori
from aplikasi.toko.serializers.kategori_serializers import KategoriSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset= Kategori.objects.all()
    serializer_class = KategoriSerializer