from django.shortcuts import render,redirect
from .forms import Myregisterform
from django.contrib import messages
from .models import stud


# from .models import Stud

def home(request):
    data=stud.objects.all()
    if data!="":
        context={'data':data}
        return render(request,'home.html',context)
    else:
        return render(request,'home.html')

def insert(request):
    if request.method =='POST':
        form=Myregisterform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration successfully completed")
            return redirect('Home')
    else:
        form=Myregisterform()
    return render(request,'register.html',{'form':form})
    

def update(request,id):
    data=stud.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['email']

        data.name=name
        data.password=password
        data.address=address
        data.contact=contact
        data.email=email
        data.save()
        messages.success(request,"Update successfully completed")
        return redirect("Home")
    return render(request,'update.html',{'data':data})

def delete(request,id):
    data=stud.objects.get(id=id)
    data.delete()
    messages.error(request,"Data deleted successfully")
    return redirect("Home")