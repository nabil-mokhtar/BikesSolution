from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
# Create your views here.
class rent:
    def index(request):
       rows= models.RentRecords.objects.all().values()
       
       return render(request,'index.html',{'rows':rows})
    def create(request):
        return render(request,'rentcreateform.html',{})
        # return HttpResponse('create f')
    def insert(request):
        new=models.RentRecords()
        new.customer=models.RentUser(id=request.POST['user']) 
        new.bike= models.Bike(id=request.POST['bike']) 
        new.starts= request.POST['starts']
        new.ends= request.POST['ends']
        new.status= request.POST['status'] #must be post-now
        new.note= request.POST['note']
        new.price= request.POST['price']
        new.save()
        return redirect('rent.index')
    def cancel(request,id):
        row=models.RentRecords(id=id)
        row.status='cancel'
        row.save()
        return redirect('rent.index')
    def extend(request,id):
        row=models.RentRecords(id=id)
        row.ends= request.POST['ends']
        row.save()
        return redirect('rent.index')