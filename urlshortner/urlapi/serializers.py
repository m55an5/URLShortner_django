from dataclasses import fields
from rest_framework import serializers
from .models import URLShortner
from .utils import generate_short_url


class URLShortnerSerializer(serializers.ModelSerializer):    
    class Meta:
        model = URLShortner
        fields = '__all__'
