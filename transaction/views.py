from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from transaction.models import Transaction
import json

class exchange(APIView):
    def get(self, request):
        return render(request, 'index.html', None)
    def post(self, request):
        return HttpResponse('Post')
    def patch(self, request):
        return HttpResponse('Patch')
    def delete(self, request):
        return HttpResponse('Del')