from django.shortcuts import render, redirect
from datetime import datetime
from first_app.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout , login
from .models import User
from django.contrib.auth.hashers import check_password , make_password
from django.contrib.auth import authenticate, login
from .models import Book


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate using the custom backend
        user = authenticate(request, username=email, password=password, backend='first_app.backends.EmailAuthBackend')

        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'index.html', {'error': 'Invalid credentials. Please try again.'})

    return render(request, 'index.html')




def signup(request):
    if request.method == 'POST':
        # Get the data from the form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        
        # Check if passwords match
        if password != password_repeat:
            return render(request, 'sign_up.html', {'error': 'Passwords do not match.'})
        hashed_password = make_password(password)
        user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
        user.save()
        return redirect('index') 
    
    return render(request, 'sign_up.html')




def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')



def b_library(request):
    return render(request, 'baiust_library.html')

def lib_policy(request):
    return render(request, 'lib_policy.html')

def member(request):
    return render(request, 'member.html')

def facility(request):
    return render(request, 'facility.html')

def lending(request):
    return render(request, 'lending.html')

def con(request):
    return render(request, 'con.html')






def search_books(request):
    query = request.GET.get('query', '')
    results = Book.objects.filter(title__icontains=query)  # Search in title
    return render(request, 'search_results.html', {'query': query, 'results': results})

