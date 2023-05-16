from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to Indian Matrimonial for NRI")

def login_users(request):
    
    return HttpResponse(" Welcome! Your Last Login date is" + str(datetime.now()))

def about(request):
    return HttpResponse("This matrimonial website is started on 2009 for NRI")

