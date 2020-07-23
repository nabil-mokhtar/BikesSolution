from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
class home:
    def index(request):
       return HttpResponse('hello')

       # return render(request,'index.html',{'rows':rows})
