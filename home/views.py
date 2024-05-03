from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1><b>Hey I am a Django Server</b></h1>")

def approval(request):
    return HttpResponse("<h1>Your request has been approved!</h1>")

def star(request):
    return HttpResponse("Star pattern is printed successfully!")

def template(request):
    names = [
        {"Name":"Rahul", "Age":24},
        {"Name":"Rohan", "Age":22},
        {"Name":"Ankit", "Age":12},
        {"Name":"Aryan", "Age":32},
        {"Name":"Keshav", "Age":16}
    ]
    text = "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Praesentium repudiandae, laboriosam voluptatibus doloremque tempora consectetur esse, perferendis necessitatibus repellendus obcaecati molestiae quis aspernatur blanditiis dolore a minima delectus non quidem."
    fruits = ["Orange","Apple","Guava","Watermelon"]
    return render(request, "index.html",context={"people":names, "text":text, "fruits":fruits})

def suc1(request):
    return render(request,"about.html")

def suc2(request):
    return render(request,"contact.html")