from django.contrib.auth.models import User
from django.shortcuts import render

students = User.objects.all()

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html', {'students': students})
