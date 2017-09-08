from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
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
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'string_gen/generator.html'

    def get(self, request, pk):
        string_generator = StringGenerator.objects.get(generator_id=pk)
        serializer = StringGeneratorSerializer(string_generator)
        template = str(serializer.data['template'])
        pars = serializer.data['par']
        template_file = serializer.data['template_file']
        if template != '':
            content = template
        elif template_file:
            content = open(template_file).read()
        else:
            content = "Error: no template to display."
        string = content.format(pars)
        return Response({'string': string})
