from rest_framework import serializers
from .models import Travel, TravelCategory, Hotel

class TravelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    price = serializers.IntegerField()
    category = serializers.SlugRelatedField(slug_field='name', queryset=TravelCategory.objects.all())
    hotel = serializers.SlugRelatedField(slug_field='name', queryset=Hotel.objects.all())

    def create(self, validated_data):
        return Travel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.hotel = validated_data.get('hotel', instance.hotel)
        instance.save()
        return instance
    
class TravelCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    
    def create(self, validated_data):
        return TravelCategory.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
    
class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    stars = serializers.IntegerField()
    price = serializers.IntegerField()
    
    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
    