from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import converter
# Create your views here.
def list_conversion_props(res):
    return render(res, 'currency_pair.html')
    

def take_base_currency(req:HttpRequest):
    currency = converter(req.POST["submit"])
    currency.save()
    return redirect('converter/')
