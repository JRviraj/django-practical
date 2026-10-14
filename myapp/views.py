from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
# Create your views here.

def home(request):
    message = "Welcome to my Django project!"
    return render(request, 'home.html', {'message': message})

