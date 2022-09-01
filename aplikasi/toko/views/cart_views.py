from rest_framework import viewsets
from aplikasi.toko.models import Keranjang
from rest_framework.decorators import action
from aplikasi.toko.serializers.cart_serializers import CartSerializer
class CartViewSet(viewsets.ModelViewSet):
    queryset=Keranjang.objects.all()
    serializer_class = CartSerializer

    @action(detail=True)
    def perform_create(self,serializer):
        serializer.save() 