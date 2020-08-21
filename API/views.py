from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Currency
from .serializers import CurrencySerializer

# Create your views here.


class CurrencyList(APIView):

    def get(self,request):
       currency=Currency.objects.all()
       serializer=CurrencySerializer(currency,many=True)
       return Response(serializer.data)


    def post(self):
      pass
