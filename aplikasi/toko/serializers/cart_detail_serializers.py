from wsgiref import validate
from rest_framework import serializers

from aplikasi.toko.models import Keranjang, KeranjangDetail, Produk
from aplikasi.toko.serializers.cart_serializers import CartSerializer

class CartDetailSerializer(serializers.ModelSerializer):

    carts= serializers.CharField(required=True)
    #customers=serializers.CharField(required=False)
    class Meta:
        model= KeranjangDetail
        fields= ('__all__')

    def create(self,validated_data):
        a=Keranjang.objects.get(id_cart=validated_data['carts'])
        total=0
        validated_data['carts']=a
        ttl=validated_data['qty_cart']*validated_data['products'].harga
        validated_data['total_harga']=ttl
        
        b=KeranjangDetail.objects.create(**validated_data)
        htg=0
        abc=KeranjangDetail.objects.filter(carts=validated_data['carts'].id_cart)
        for i in abc:
            htg+=i.total_harga
        
        Keranjang.objects.filter(id_cart=validated_data['carts'].id_cart).update(total_cart=htg)
        return b
    # def create(self,validated_data):
          
    #     val= validated_data.pop('carts')
    #     ab= validated_data.pop('a')
    #     b=Keranjang.objects.create(**val)
    #     total=0
        
    #         dt['carts']=b
    #         ttl= dt['qty_cart']*dt['products'].harga
    #         dt['total_harga']=ttl
    #         total += ttl
    #         a= KeranjangDetail.objects.create(**dt)
    #     Keranjang.objects.filter(id_cart=b).update(total_cart=total)
    #     return a
    def to_representation(self, instance):
          response = super().to_representation(instance)
          response['carts']= instance.carts.id_cart
          return response
