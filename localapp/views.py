from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from pymongo import MongoClient
from django.contrib.auth.forms import UserCreationForm


client = MongoClient("mongodb://localhost:27017/")
mongo_db = client["localpal_db"]
users_collection = mongo_db["users"]
feedbacks_collection = mongo_db["feedbacks"]

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in after registering
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'localapp/register.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if users_collection.find_one({'username': username}):
            messages.error(request, "Username already exists")
            return render(request, 'localapp/register.html')

        # store user in Mongo
        users_collection.insert_one({
            'username': username,
            'email': email,
            'password': make_password(password)
        })
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

    return render(request, 'localapp/register.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_doc = users_collection.find_one({'username': username})

        if user_doc and check_password(password, user_doc['password']):
            # log them in using Django session
            request.session['username'] = username
            messages.success(request, "Logged in successfully")
            return redirect('explore')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'localapp/login.html')

def logout_view(request):
    request.session.flush()
    messages.success(request, "Logged out.")
    return redirect('login')

@login_required
def explore(request):
    if request.method == 'POST':
        feedback_text = request.POST['feedback']
        feedbacks_collection.insert_one({
            'user': request.session['username'],
            'text': feedback_text
        })
        messages.success(request, "Feedback submitted!")

    return render(request, 'localapp/explore.html') 

def home(request):
    return render(request, 'localapp/home.html')
