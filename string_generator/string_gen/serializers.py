from rest_framework import serializers
from .models import StringGenerator


class StringGeneratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = StringGenerator
        fields = ('template', 'par')
