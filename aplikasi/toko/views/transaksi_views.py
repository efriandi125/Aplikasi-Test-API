
from rest_framework import viewsets
from aplikasi.toko.models import Produk, Transaksi
from rest_framework.decorators import action
from rest_framework.response import Response
from aplikasi.toko.serializers.transaksi_serializers import TransaksiSerializer
from aplikasi.toko.serializers.transaksi_data_serializers import TransaksiDataSerializer
class TransaksiViewSet(viewsets.ModelViewSet):
    queryset= Transaksi.objects.all()
    serializer_class = TransaksiSerializer

    # @action(detail=False,methods=['get'])
    # def get_data(self,request):
    #   serializer=TransaksiSerializer(many=True)
        
    # return Response(serializer.data)