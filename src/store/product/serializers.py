from rest_framework import serializers
from .models import Allproduct

class AllproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allproduct
        fields = ('id', 'product_name', 'product_price')