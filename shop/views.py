from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import Category, Product
from shop.serializer import CategorySerializer, ProductSerializer

class CategoryView(APIView):

    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class ProductView(APIView):

    def get(self, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
