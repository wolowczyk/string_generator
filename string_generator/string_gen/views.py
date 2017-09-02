from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StringGenerator
from .serializers import StringGeneratorSerializer


#/stringgenerators
class StringGeneratorList(APIView):

    def get(self, request):
        string_generators = StringGenerator.objects.all()
        serializer = StringGeneratorSerializer(string_generators, many=True)
        return Response(serializer.data)


#/stringgenerators/pk
class StringGeneratorView(APIView):

    def get(self, request, pk):
        string_generator = StringGenerator.objects.get(generator_id=pk)
        serializer = StringGeneratorSerializer(string_generator)
        return Response(serializer.data)
