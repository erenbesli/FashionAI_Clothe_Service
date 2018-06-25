from django.shortcuts import render

# Create your views here.

from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet


from .models import *
from .serializers import *


class GetAllClotheImagesView(APIView):
    def post(self, request):
        clothe = clothe_images.objects.all()
        serializer = ClotheImageModelSerializer(clothe, many=True)

        # run the crawler method to store crawled data to mongodb

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostClotheImagesView(APIView):
    def post(self, request):
        # Modify Serializer according to crawler data
        serializer = ClotheImageModelSerializer(data=request.data)

        # run the crawler method to store crawled data to mongodb

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, clotheId=0, category=""):
    #
    #     query= {}
    #     if clotheId != "0":
    #         query['product_code'] = clotheId
    #     if category != "0":
    #         query['category'] = category
    #
    #
    #
    #     if category != "0" and clotheId != "0":
    #         clothe = clothe_images.objects.all()
    #         serializer = ClotheImageModelSerializer(clothe, many=True)
    #     else:
    #         clothe = clothe_images.objects(__raw__=query)
    #
    #     serializer = ClotheImageModelSerializer(clothe, many=True)
    #     return Response(serializer.data)





