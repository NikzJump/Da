from rest_framework import serializers
from .models import Warehouse, Product, Group


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    titles = ProductSerializer(many=True)

    class Meta:
        model = Warehouse
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    titles = ProductSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'
