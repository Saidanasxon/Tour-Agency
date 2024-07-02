from rest_framework import serializers
from .models import Travel, TravelCategory, Hotel

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'


class TravelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelCategory
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'