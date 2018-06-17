from rest_framework.serializers import ModelSerializer

from ads.models import Post


class PostListSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['id', 'titulo', 'texto', 'URLimagen']


class NewPostSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['blog','categorias', 'titulo', 'texto', 'cuerpo', 'URLimagen']


class PostDetailSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = '__all__'