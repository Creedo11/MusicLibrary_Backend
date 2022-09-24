from django.http import Http404
from .models import Music
from .serializers import MusicSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from music import serializers

# Create your views here.
class MusicList(APIView):

    def get(self, request):
        songs = Music.objects.all()
        serializer = MusicSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
