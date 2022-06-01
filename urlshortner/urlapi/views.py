from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import URLShortnerSerializer
from .models import URLShortner
from .utils import generate_short_url
from django.shortcuts import redirect
import urllib.parse


class CreateURLShortner(APIView):
    def post(self, request):
        short_url = generate_short_url(URLShortner)
        request.data.update({'short_url': short_url})
        encoded_url = urllib.parse.unquote(request.data['original_url'])
        request.data.update({'original_url': encoded_url})
        print("REQUEST UEL:", request.data)
        serializer = URLShortnerSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            short_url = "http://localhost:8000/" + serializer.data['short_url']
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class GetShortURL(APIView):
    def get(self, request, short_url):
        url_query_set = URLShortner.objects.filter(short_url=short_url)

        if not url_query_set.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return redirect(url_query_set[0].original_url)