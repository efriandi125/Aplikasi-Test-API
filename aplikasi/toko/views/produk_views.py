from aplikasi.toko.models import Produk
from rest_framework import viewsets

from aplikasi.toko.serializers.produk_serializers import ProdukSerializer

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer