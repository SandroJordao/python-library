from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Authors, Books
from .serializers import AuthorsSerialize, BooksSerialize


class ResultsSetPagination(PageNumberPagination):
    """
    Defines the attributes of a pagination
    """
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class AuthorsApi(ModelViewSet):
    """ 
    Author API Endpoints 
    Defining filters, pagination and ordering of a author
    """
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerialize
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['name']
    ordering = ['-id']


class BooksApi(ModelViewSet):
    """ 
    Book API Endpoints 
    Defining filters, pagination and ordering of a book
    """
    queryset = Books.objects.all()
    serializer_class = BooksSerialize
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'edition', 'publication_year', 'authors__name']
    ordering_fields = '__all__'
    ordering = ['-id']
