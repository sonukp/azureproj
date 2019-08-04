from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from azureapp.client import Client
from . import settings


# Create your views here.


@api_view(['GET', 'POST'])
def getqueue(request):
    if request.method == 'GET':
        c = Client(settings.CLIENT_ID, settings.SECRET, settings.TENANT_ID)
        print(c.get_token())
        return Response(c)

