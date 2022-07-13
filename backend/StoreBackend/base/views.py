from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
# from .products import products
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

routes = [
    '/api/v1/products/',
    '/api/v1/products/create',

    '/api/v1/products/upload/',

    '/api/v1/products/<id>/reviews/',

    '/api/v1/products/top/',
    '/api/v1/products/<id>/',

    '/api/v1/products/delete/<id>/',
    '/api/v1/products/<update>/<id>/',

]


@api_view(http_method_names=['GET'])
def getRoutes(request):
    return Response(routes)


@api_view(http_method_names=['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def getProducts(request):
    products = Product.objects.all()
    # print(products)
    serializer = ProductSerializer(products, many=True)
    # print(serializer.data)
    return Response(serializer.data)
