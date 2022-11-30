from rest_framework.serializers import ModelSerializer, SerializerMethodField
from shop.models import Article, Category, Product

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']

class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category']

class ProductDetailSerializer(ModelSerializer):

    articles = SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category', 'articles']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data

class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name']

class CategoryDetailSerializer(ModelSerializer):

    products = SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']
    
    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductSerializer(queryset, many=True)
        return serializer.data