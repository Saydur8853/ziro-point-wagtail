from django.shortcuts import render
from .serializers import SettingsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class SettingsAPIView(APIView):

    def get(self, request, format=None):
        return Response(SettingsSerializer({}, context={"request": request}).data)
