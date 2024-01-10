from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    peoples = [
        {"Name" : "Adarsh varma" , "Age" : 24},
        {"Name" : "Nitin Sirsath" , "Age" : 23},
        {"Name" : "Swaraj Chandu" , "Age" : 25},
        {"Name" : "Mitanshu Salvi" , "Age" : 26},
        {"Name" : "Anurag Varma" , "Age" : 21},
    ]

    return render(request,"index.html", context = {'peoples' : peoples})
