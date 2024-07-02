from rest_framework.exceptions import ValidationError
from django.shortcuts import render
from .models import Travel, TravelCategory, Hotel
from .serializers import TravelSerializer, TravelCategorySerializer, HotelSerializer
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)

class TravelListApiView(ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class TravelDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class TravelCategoryListApiView(ListCreateAPIView):
    queryset = TravelCategory.objects.all()
    serializer_class = TravelCategorySerializer

class TravelCategoryDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = TravelCategory.objects.all()
    serializer_class = TravelCategorySerializer

class HotelListApiView(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    