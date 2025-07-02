import json
from decimal import Decimal

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter

from django.db.models import Min, Max, Q
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

from .serializers import *


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryShortSerializer

class CasesListView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseShortSerializer

class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name_slug'

class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'name_slug'

