from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    """
    Serializer for the House model.
    """
    class Meta:
        model = House
        fields = '__all__'
        read_only_fields = ('id',)
