from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("My first Django Project")

def index(request):
    #my_dict = {'insert_me': "Hello im views.py!"}
    return render(request,'index.html')

def signup(request):
    return render(request,'sign_up.html')