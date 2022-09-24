from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from django.http.response import JsonResponse
from .models import converter
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from converter.models import converter,signup
from converter.serializers import TodoSerializer,SignUpSerializer

# Create your views here.
@csrf_exempt
def todo(request,id=0):
    convert = converter.objects.all()
    serializer = SignUpSerializer(convert, many=True)
    JsonResponse(serializer.data)
    
def list_conversion_props(res):
    return render(res, 'currency_pair.html')
    

def take_base_currency(req:HttpRequest,id=0):
    currency = converter(req.POST["submit"])
    currency.save()
    return redirect('converter/')
