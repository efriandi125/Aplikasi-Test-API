from rest_framework import serializers

from aplikasi.toko.models import Customer, Keranjang, Produk, Transaksi
from aplikasi.toko.serializers.cart_serializers import CartSerializer
from aplikasi.toko.serializers.produk_serializers import ProdukSerializer
from aplikasi.toko.serializers.transaksi_serializers import TransaksiSerializer

class CustomerSerializer(serializers.ModelSerializer):
   # cart= TransaksiSerializer(write_only=True,many=True)
 

    class Meta:
        model = Customer
        fields = '__all__'
    
  
        
    def create(self,validated_data):  
        #val= validated_data.pop('cart') 
        head= Customer.objects.create(**validated_data)     
        # ttl=0
  
        # for x in val:
        #     ttl=x['Qty_trans'] * x['Produks'].Harga
        #     brg= Produk.objects.get(Id_Produk=x['Produks'].Id_Produk)
        #     if(brg.Qty>= x['Qty_trans']):
        #         brg.Qty -= x['Qty_trans']
        #         brg.save()
                
        #     x['Total']=ttl
        #     x['Customers']=head
            
        #     Transaksi.objects.create(**x)
       
        return head
         