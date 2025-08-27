from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit 

def home_page(request):
    query_set = PageVisit.objects.all()

    return render(request,'home.html')