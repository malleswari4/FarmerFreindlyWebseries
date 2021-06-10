from django.shortcuts import render,redirect
from django.http import HttpResponse
from farmer.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'farmer/index.html')
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        upass=request.POST['upass']
        user_details=registerdb.objects.get(mail=request.POST['email'])
        name=user_details.name
        
        try:
            data=registerdb.objects.get(mail=request.POST['email'],regpass=request.POST['upass'])
            if data:
                return render(request,'farmer/profile.html',{'name':name})
        except Exception:
            return HttpResponse("Wrong Credentionals ...!!!")
        # if data.mail==request.POST['email'] and data.regpass==request.POST['upass']:
        #     return render(request,'farmer/profile.html',{'name':name})
        # elif data.mail!=request.POST['email'] and data.regpass==request.POST['upass']:
        #     return HttpResponse("Login Failed")
        # elif data.mail==request.POST['email'] and data.regpass!=request.POST['upass']:
        #     return HttpResponse("Login Failed")
        # elif data.mail!=request.POST['email'] and data.regpass!=request.POST['upass']:
        #     return HttpResponse("Login Failed")    
        # else:
        #     return HttpResponse("Login Failed")
    return render(request,'farmer/login.html')
def signup(request):
    messages.success(request,"Welcome to SignUP")
    if request.method=="POST":
        fname=request.POST['username']
        femail=request.POST['email']
        fland=request.POST['land']
        fphone=request.POST['phone']
        fpass=request.POST['password']
        details=registerdb(name=fname,mail=femail,land=fland,phone=fphone,regpass=fpass)
        details.save()
        messages.success(request,"Registered successfully")
    return render(request,'farmer/signup.html')
    messages.error(request,"Registered Failed")
def contact(request):
    return render(request,'farmer/contact.html')
def crops(request):
    return render(request,'farmer/crops.html')
def pestisides(request):
    return render(request,'farmer/pestisides.html')
def about(request):
    return render(request,'farmer/about.html')
def workers(request):
    users=userdb.objects.all()
    return render(request,'farmer/users.html',{'data':users})    
def paddy(request):
    return render(request,'farmer/paddy.html')
def sugarcane(request):
    return render(request,'farmer/sugarcane.html')
def tomato(request):
    return render(request,'farmer/tomato.html')
def watermelon(request):
    return render(request,'farmer/watermelon.html')
def brinjal(request):
    return render(request,'farmer/brinjal.html')
def users(request):
    return render(request,'farmer/users.html')