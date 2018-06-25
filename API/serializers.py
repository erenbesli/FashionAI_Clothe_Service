from rest_framework_mongoengine import serializers

from .models import *


class Clothe_Image_Serializer(serializers.DocumentSerializer):
    class Meta:
        model = Clothe_Image
        fields = '__all__'


class Clothe_Image_Inferred_Serializer(serializers.DocumentSerializer):
    class Meta:
        model = Clothe_Image_Inferred
        fields = '__all__'