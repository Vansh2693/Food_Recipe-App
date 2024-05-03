from django.shortcuts import render,redirect
from .models import *

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