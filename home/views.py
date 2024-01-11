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

    return render(request,"index.html", context = {'peoples' : peoples})

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
