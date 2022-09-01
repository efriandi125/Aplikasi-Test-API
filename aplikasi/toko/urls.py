from rest_framework.routers import DefaultRouter
from django.urls import path,include
from aplikasi.toko.views.cart_detail_views import CartDetailViewSet
from aplikasi.toko.views.cart_views import CartViewSet
from aplikasi.toko.views.customer_views import CustomerViewSet
from aplikasi.toko.views.kategori_views import KategoriViewSet

from aplikasi.toko.views.produk_views import ProdukViewSet

from aplikasi.toko.views.transaksi_views import TransaksiViewSet
from django.contrib import admin

router= DefaultRouter()
router.register(r'produk',ProdukViewSet,basename='produk')
router.register(r'transaksi',TransaksiViewSet,basename='transaksi')
router.register(r'kategori',KategoriViewSet,basename='kategori')
router.register(r'customer',CustomerViewSet,basename='customer')
router.register(r'cart',CartViewSet,basename='cart')
router.register(r'cart_detail',CartDetailViewSet,basename='cart_detail')

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include(router.urls))
]
