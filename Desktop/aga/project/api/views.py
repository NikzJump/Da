from .models import Product, Warehouse, Group
from .serializer import ProductSerializer, WarehouseSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_warehouse_products(request, pk):
    try:
        warehouse = Warehouse.objects.get(pk=pk)
    except:
        return Response({"error": "code: 404"})

    serializer = WarehouseSerializer(warehouse)

    data = []
    cnt = 0
    for i in serializer.data['titles']:
        cnt += 1
        data.append({
            'id': cnt,
            'title': i['title'],
            'num_war': i['num_war'],
            'num_group': ['num_group'],
        })

    return Response({"data": data})


@api_view(["GET"])
def get_group_products(request, pk):
    try:
        group = Warehouse.objects.get(pk=pk)
    except:
        return Response({"error": "code: 404"})

    serializer = WarehouseSerializer(group)

    data = []
    cnt = 0
    for i in serializer.data['titles']:
        cnt += 1
        data.append({
            'id': cnt,
            'title': i['title'],
        })

    return Response({"data": data})


@api_view(["GET"])
def get_prod(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except:
        return Response({"code 404"})

    serializer = ProductSerializer(product)

    return Response({"data": serializer.data})
