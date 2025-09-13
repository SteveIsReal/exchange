from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import generics
from transaction.models import Transaction
from transaction.serial import TransactionSerializer
import json

class Exchange(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class Login(APIView):
    def get(self, request):
        return render(request, 'login_page.html', None)
    def post(self, request):
        return render(request, 'index.html', None)



