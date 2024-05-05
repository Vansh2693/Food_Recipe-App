from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def receipes(request):
    if request.method=="POST":
        data = request.POST
        rec_name = data.get("receipe_name")
        rec_desc = data.get("receipe_description")
        rec_img = request.FILES.get("receipe_img")
        
        Receipe.objects.create(
            receipe_name = rec_name,
            receipe_description = rec_desc,
            receipe_img = rec_img
        )
        
        return redirect("/receipes/")
    
    queryset = Receipe.objects.all()
    if request.GET.get("search"):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get("search"))
    
    context = {"Receipe":queryset}
    return render(request,"receipes.html",context)

def delete_recipes(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    
    return redirect("/receipes/")

def update_recipes(request,id):
    queryset = Receipe.objects.get(id=id)
    
    if request.method=="POST":
        data = request.POST
        rec_name = data.get("receipe_name")
        rec_desc = data.get("receipe_description")
        rec_img = request.FILES.get("receipe_img")
        
        queryset.receipe_name = rec_name
        queryset.receipe_description = rec_desc
        if queryset.receipe_img:
            queryset.receipe_img = rec_img
        queryset.save()
        return redirect("/receipes/")
    
    context = {"Receipe":queryset}
    return render(request,"update_recipes.html",context)

def login_page(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username!")
            return redirect("/login/")
        
        user = authenticate(username= username, password = password)
        
        if user is None:
            messages.info(request, "Invalid Password!")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/receipes/")
        
    return render(request, "login.html")

def logout_page(request):
    logout(request)
    return redirect("/login/")
def register_page(request):
    
    if request.method=="POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "User Already Exist!")
            return redirect("/register/")
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        
        user.set_password(password)
        user.save()
        messages.info(request, "User created Successfully")
        return redirect("/register/")
    return render(request, "register.html")