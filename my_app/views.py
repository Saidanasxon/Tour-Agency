from rest_framework.exceptions import ValidationError
from django.shortcuts import render
from .models import Travel, TravelCategory, Hotel
from .serializers import TravelSerializer, TravelCategorySerializer, HotelSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

class TravelAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                return Response(TravelSerializer(travel).data)
            except:
                return Response({"error": "Not Found"})
        travel = Travel.objects.all()
        return Response({"travels": TravelSerializer(travel, many=True).data})
    
    def post(self, request: Request):
        serializer = TravelSerializer(data=request.data)
        if serializer.is_valid():
            travel = serializer.save()
            return Response(TravelSerializer(travel).data)
        else:
            return Response(serializer.errors, status=400)

    
    def put(self, request: Request, pk: int = None):
        if not pk:
            return Response({"error": "Method PUT Not Allowed"})
        try:
            travel = Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            return Response({"error": "Not Found"}, status=404)
        
        try:
            serializer = TravelSerializer(instance=travel, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_travel = serializer.save()
            return Response(TravelSerializer(updated_travel).data)
        except ValidationError as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": "An unexpected error occurred: " + str(e)}, status=500)
        
    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({"error": "Method DELETE Not Allowed"})
        try:
            travel = Travel.objects.get(pk=pk)
            travel.delete()
            return Response({"deleted": True})
        except:
            return Response({"error": "Not Found"})
        
class TravelCategoryAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                travel_category = TravelCategory.objects.get(pk=pk)
                return Response(TravelCategorySerializer(travel_category).data)
            except:
                return Response({"error": "Not Found"})
        travel_category = TravelCategory.objects.all()
        return Response({"travel_categories": TravelCategorySerializer(travel_category, many=True).data})
    
    def post(self, request: Request):
        serializer = TravelCategorySerializer(data=request.data)
        serializer.is_valid()
        travel_category = serializer.save()
        return Response(TravelCategorySerializer(travel_category).data)
    
    def put(self, request: Request, pk: int = None):
        if not pk:
            return Response({"error": "Method PUT Not Allowed"}, status=405)
        
        try:
            travel_category = TravelCategory.objects.get(pk=pk)
        except TravelCategory.DoesNotExist:
            return Response({"error": "Travel Category Not Found"}, status=404)
        
        serializer = TravelCategorySerializer(instance=travel_category, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            updated_travel_category = serializer.save()
            return Response(TravelCategorySerializer(updated_travel_category).data)
        except ValidationError as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": "An unexpected error occurred: " + str(e)}, status=500)
    
    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({"error": "Method DELETE Not Allowed"})
        try:
            travel_category = TravelCategory.objects.get(pk=pk)
            travel_category.delete()
            return Response({"deleted": True})
        except:
            return Response({"error": "Not Found"})
        
class HotelAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                hotel = Hotel.objects.get(pk=pk)
                return Response(HotelSerializer(hotel).data)
            except:
                return Response({"error": "Not Found"})
        hotel = Hotel.objects.all()
        return Response({"hotels": HotelSerializer(hotel, many=True).data})
    
    def post(self, request: Request):
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid()
        hotel = serializer.save()
        return Response(HotelSerializer(hotel).data)
    
    def put(self, request: Request, pk: int = None):
        if not pk:
            return Response({"error": "Method PUT Not Allowed"}, status=405)
        
        try:
            hotel = Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            return Response({"error": "Hotel Not Found"}, status=404)
        
        serializer = HotelSerializer(instance=hotel, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            updated_hotel = serializer.save()
            return Response(HotelSerializer(updated_hotel).data)
        except ValidationError as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": "An unexpected error occurred: " + str(e)}, status=500)
        
    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({"error": "Method DELETE Not Allowed"})
        try:
            hotel = Hotel.objects.get(pk=pk)
            hotel.delete()
            return Response({"deleted": True})
        except:
            return Response({"error": "Not Found"})
        
        
