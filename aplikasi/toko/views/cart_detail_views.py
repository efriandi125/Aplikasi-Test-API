from rest_framework import viewsets

from aplikasi.toko.models import KeranjangDetail
from aplikasi.toko.serializers.cart_detail_serializers import CartDetailSerializer

class CartDetailViewSet(viewsets.ModelViewSet):
    queryset=KeranjangDetail.objects.all()
    serializer_class= CartDetailSerializer