from rest_framework_mongoengine import serializers

from .models import *


class ClotheImageModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = clothe_images
        fields = '__all__'


