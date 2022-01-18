from django.contrib.auth import forms
from django.http import response
from django.http.response import HttpResponseRedirect, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from sem5.forms import RegisterForm


from django.core.files.storage import default_storage

from sem5.serializers import uscoreSerializer
# Create your views here.

def index(request):
    return render(request, "users/index.html")
def sighin(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html",{
            "message" : "Try logging in first"  
        })  
    return render(request, "users/user.html")       
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("welcome"))
        else:
            return render(request, "users/login.html",{
            "message" : "Invalid, credentials!"
            })
    return render(request, "users/login.html")
def logout_view(request):
    return render(request, "users/login.html",{
        "message" : "Logged out Sucessfully."
    })   
def play(request):
    if request.method == 'POST':
        uscores = JSONParser.parse(request)
        uscore_serializer = uscoreSerializer(data = uscores)
        if uscore_serializer.is_valid:
            uscore_serializer.save()
            return JsonResponse("Added, Sucessfully!", safe=False) 
        return JsonResponse("Fail To Add", safe=False)
    if not request.user.is_authenticated:
        return render(request,"users/login.html ", {
            "message" : "Try logging in first"
        })
    return render(request, "users/play.html")
def lvl(request):
    if request.method == 'POST':
        uscores = JSONParser.parse(request)
        uscore_serializer = uscoreSerializer(data = uscores)
        if uscore_serializer.is_valid():
            uscore_serializer.save()
            return JsonResponse("Added, Sucessfully!", safe=False) 
        return JsonResponse("Fail To Add", safe=False)
    if not request.user.is_authenticated:
        return render(request,"users/login.html ", {
            "message" : "Try logging in first"
        })
    return render(request, "users/lvl.html")
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "users/login.html",{
                 "message" : "Registered Sucessfully"
            })
           
        else:
            return render(request, "users/login.html",{
            "message" : "Registration Failed"
            })
    else:
        form=RegisterForm()
        return render(request , "users/register.html" , {
            "form":form ,
            "message" : "Register to Create Account"
            
            } )
def welcome(request) :
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"),{
            "message" : "Try logging in first"
        })
    return render(request, "users/welcome.html")
def profile(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html",{
            "message" : "Try logging in first"  
        })
    return render(request, "users/profile.html")

