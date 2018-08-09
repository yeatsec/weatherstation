from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *

# Create your views here.

def home(request):
	return HttpResponse('welcome home!')
