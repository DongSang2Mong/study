from django.shortcuts import render
from django.http import HttpResponse

def printDongSang(request):
    return HttpResponse("Hello 동상이몽")