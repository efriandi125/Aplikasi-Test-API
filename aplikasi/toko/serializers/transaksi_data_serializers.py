from rest_framework import serializers

from aplikasi.toko.models import KeranjangDetail, Transaksi
class TransaksiDataSerializer(serializers.ModelSerializer):
    carts= serializers.PrimaryKeyRelatedField(read_only=True,required=False)
    produks=serializers.SerializerMethodField(required=False)

    class Meta:
        model=Transaksi
        fields= '__all__'

    def get_transaksi(self,obj):
        d=Transaksi.objects.all()
        return d
    def get_produks(self,obj):
        a=Transaksi.objects.all().select_related('carts').select_related('products').get(carts=obj.id_transaksi)
        for i in a:
            var=i.products
        return var