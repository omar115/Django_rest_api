from django.db.models import manager
from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response


# Create your views here.

# class based view

class StatusAPIView(APIView):
    def get(self, request, format=None):
        status_list = Status.objects.all()
        status_serializer = StatusSerializer(status_list, many=True)
        return Response(status_serializer.data)


# In APIView we need to specify the get method, but in ListAPIView, we do not need to specify the 
# get method, we just need to put the queryset (means you need to mention the model name that you  need to query)
# and serializer_class (means you need to mention the serializer name to serialize the data)
class StatusListApiView(ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusCreateApiView(CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

# RetrieveAPIView will give you access to see single status by searching with unique entry
class StatusDetailApiView(RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

# difference between PUT and PATCH --> PUT: you have to send the full object to update one entry
# PATCH: you just need to send the updated entry, not full object
# UpdateAPIView will support both PUT and PATCH but not GET method

class StatusUpdateApiView(UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'


class StatusDeleteApiView(DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'