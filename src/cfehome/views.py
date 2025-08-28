from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit 

def home_page(request):
    return render(request,'home.html')