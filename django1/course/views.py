from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

list1=[
    {"name":"c"},
    {"name":"c#"},
    {"name":"python"}
]
def courses(request,name):
    data=""
    for item in list1:
        data=data+{item['name']}
    return HttpResponse(data)