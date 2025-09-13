from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from transaction.models import Transaction
from transaction.serial import TransactionSerializer
import json

class Exchange(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class EditExchange(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'id'

class Calculate(APIView):
    def get(self, request):
        all_amount = 0
        for i in Transaction.objects.all():
            if i.type == "input":
                all_amount += i.amount
            else:
                all_amount -= i.amount
        return Response(status=status.HTTP_200_OK, data=all_amount)

class Login(APIView):
    def get(self, request):
        return render(request, 'login_page.html', None)
    def post(self, request):
        return render(request, 'index.html', None)



