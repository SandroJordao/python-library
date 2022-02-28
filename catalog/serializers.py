from rest_framework.serializers import ModelSerializer
from .models import Authors, Books


class AuthorsSerialize(ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class BooksSerialize(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
