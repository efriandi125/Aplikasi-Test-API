from asyncore import write
from rest_framework import serializers

from aplikasi.toko.models import Customer, Keranjang, KeranjangDetail, Produk, Transaksi
from aplikasi.toko.serializers.produk_serializers import ProdukSerializer

class CartSerializer(serializers.ModelSerializer):
    #products=ProdukSerializer(many=True,read_only=True)
    #total_cart= serializers.SerializerMethodField
    class Meta:
        model = Keranjang
        fields = ('__all__')
    
    # def create(self,validated_data):
    #     val=validated_data.pop('detail')
    #     b=Keranjang.objects.create(**validated_data)
    #     total=0
    #     for x in val:
    #         x['carts']=b
    #         ttl= x['qty_cart']*x['products'].harga
    #         x['total_harga']=ttl
    #         total += ttl
    #     a= KeranjangDetail.objects.create(**x)
    #     Keranjang.objects.filter(id_cart=b).update(total_cart=total)
    #     return a
    # def create(self,validated_data):
    #    # val= validated_data.pop("products",[])
    #     row= validated_data.products.all()

    #     for i in val:

    #         #validated_data['products']=datas


    #         obj_data= Keranjang.objects.create(**i,**validated_data)
        # return obj_data

   


