from rest_framework import serializers
from ecommerceapp.models import ProductMstModel

class AllProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductMstModel
        fields = ['id','code','desc','price']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductMstModel
        fields = ['__all__']
