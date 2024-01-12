from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    peoples = [
        {"Name" : "Adarsh varma" , "Age" : 24},
        {"Name" : "Nitin Sirsath" , "Age" : 23},
        {"Name" : "Swaraj Chandu" , "Age" : 18},
        {"Name" : "Mitanshu Salvi" , "Age" : 12},
        {"Name" : "Anurag Varma" , "Age" : 21},
        {"Name" : "Aarohi Varma" , "Age" : 2},
    ]

    return render(request,"index.html", context = {'peoples' : peoples ,"page" : "Django Application"})

def contact(request):
    context = {'page' : "contact"}
    return render(request, "contact.html", context)

def about(request):
    context = {'page' : "about"}
    return render(request, "about.html", context)
