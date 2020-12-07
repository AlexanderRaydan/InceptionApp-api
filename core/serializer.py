from rest_framework import serializers
from api.models import InceptionImageModel

class InceptionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InceptionImageModel 
        fields = ['id' , 'image']