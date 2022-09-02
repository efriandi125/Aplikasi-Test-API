from rest_framework import viewsets
from aplikasi.toko.models import Customer
from aplikasi.toko.serializers.customer_serializers import CustomerSerializer
class CustomerViewSet(viewsets.ModelViewSet):
    queryset= Customer.objects.all()
    serializer_class = CustomerSerializer