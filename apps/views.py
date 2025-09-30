from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, CreateAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.filters import ProductFilter
from apps.models import *
from apps.serializers import (
    BookListModelSerializer, AuthorListModelSerializer, ProductListModelSerializer
)


class BookListAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListModelSerializer
    permission_classes = IsAuthenticated,


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)


