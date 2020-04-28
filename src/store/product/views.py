from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Home(request):
    return render(request,'product/home.html')
    #return HttpResponse('<h1>Hello world</h1>')

def About(request):
    return render(request,'product/about.html')
    
#########API##############

from django.http import JsonResponse
from .serializers import AllproductSerializer
from .models import Allproduct

def APIAllproduct(request):
    allproduct = Allproduct.objects.all()
    #print(allproduct)
    serializer = AllproductSerializer(allproduct, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii':False})


def APIProduct(request, pk):
    singleproduct = Allproduct.objects.get(id=pk)
    serializer = AllproductSerializer(singleproduct)
    return JsonResponse(serializer.data, safe=True, json_dumps_params={'ensure_ascii':False})

##########################