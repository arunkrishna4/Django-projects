from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("hello guys welcome to my channel")

def login(request):
    return HttpResponse("u r not allowed")

def article(request):
    return HttpResponse(''' Data mining is the process of extracting useful information from large sets of data. 
It involves using various techniques from statistics, machine learning, and database systems to identify patterns, relationships, and trends in the data.
“Data Mining” can be referred to as knowledge mining from data, knowledge extraction, data/pattern analysis.

Data mining is a crucial component of successful analytics initiatives in organizations. 
The information it generates can be used in business intelligence (BI) and advanced analytics applications that involve analysis of historical data, as well as 
Real-time analytics applications that examine streaming data as it's created or collected.

''')