from rest_framework.response import Response

from django.http import JsonResponse,HttpResponse
from rest_framework import serializers

from aplikasi.toko.models import Customer, Keranjang, KeranjangDetail, Produk, Transaksi
from aplikasi.toko.serializers.cart_serializers import CartSerializer
from aplikasi.toko.serializers.produk_serializers import ProdukSerializer


class TransaksiSerializer(serializers.ModelSerializer):
    qty_trans= serializers.IntegerField(required=False)
    total = serializers.IntegerField(required=False)
    produk= serializers.SerializerMethodField(required=False)
 
   
    

    class Meta:
        model = Transaksi
        fields = '__all__'

  
    def get_produk(self,obj):
        
        b=Produk.objects.filter(keranjangdetail__carts__transaksi=obj)
        # a=KeranjangDetail.objects.filter(carts=obj.carts.id_cart)
        return ProdukSerializer(b, many=True).data
        # for x in range(len(b)):
        #     var= b[x]
        # return var.id_Produk
        # for x in a:
        #     for i in b:
        #         var=i.id_Produk
        # return var

  
    def create(self,validated_data):
        total=0
        obj_cart= Keranjang.objects.get(customers=validated_data['customers'].id_customer,status=True)
        obj_deta=KeranjangDetail.objects.filter(carts=obj_cart.id_cart)
        
        for i in obj_deta:  
           
            
            total+= i.qty_cart 
            validated_data['qty_trans']=total
        validated_data['carts']=obj_cart
        validated_data['customers']=obj_cart.customers
        validated_data['total']=obj_cart.total_cart
        end= Transaksi.objects.create(**validated_data) 
        if(obj_deta.qty_cart<= obj_deta.products.qty):
              obj_deta.products.qty -= obj_deta.qty_cart
              obj_deta.products.save()
        elif(obj_deta.qty_cart>= obj_deta.products.qty):
              print("Stok tidak memenuhi")     
        return end
    # def create(self,validated_data):
    #     #Carts= validated_data.pop('Carts')
    
    #     obj_cart= Keranjang.objects.get(id_cart=validated_data['carts'])
    #     obj_customer= obj_cart.customers
    #     obj_prd= obj_cart.products
    
    #     if(obj_cart.qty_cart>= obj_prd.qty):
    #           obj_prd.qty -= obj_cart.qty_cart
    #           obj_prd.save()
        
    #     validated_data['qty_trans']=obj_cart.qty_cart  
    #     validated_data['customers']=obj_customer
    #     validated_data['produks']=obj_prd
    #     ttl=0 
    #     ttl=validated_data['qty_trans'] * obj_cart.products.harga
    #     validated_data['carts']=obj_cart
        
    #     validated_data['total']=ttl
        
        
    #     return Transaksi.objects.create(**validated_data)
    
    # def to_representation(self, instance):
    #       response = super().to_representation(instance)
    #       response['carts']= instance.carts.id_cart
    #       return response