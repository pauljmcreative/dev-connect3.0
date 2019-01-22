import re
from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from dev_connect.models import StudentProfile

strong = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})")

def register(request):
    print('IN REGISTER')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

    ######DO PASSWORDS MATCH?#########
        if password == password2:
            print('IN PASSWORD')
            ##### IS THIS PASSWORD VALID? #####
            # if strong.match(password):
            #     #####DOES USERNAME EXIST ALREADY?#######
            #     print('IN STRONG PASSWORD')
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/register.html', {'error': 'Username already registered.  Please choose a different username.'})
            else:
                #####CHECK FOR EMAIL######
                # print('IN CHECK EMAIL')
                # if User.objects.filter(email=email).exists():
                #     return render(request, 'accounts/register.html', {'error': 'That email has already been registered.'})
                #     #########REGISTER USER#######
                # else:
                print('IN CREATE USER')
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                profile = StudentProfile.objects.create(user_id=user)
                new_user = auth.authenticate(username=username,password=password)
                auth.login(request, user)
                return HttpResponseRedirect("../../students/profile/edit")
            # else:
            #     return render(request, 'accounts/register.html', {'error': 'Password requires an uppercase letter, a lowercase letter, a number, and a special character(!@#\$%\^&).'})
        else:
            return render(request, 'accounts/register.html', {'error': 'Passwords do not match.'})
    else:
        return render(request, 'accounts/register.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('student_profile', username=username)
    else:
      return render(request, 'accounts/login.html', {'error': 'Invalid credentials.'})
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  auth.logout(request)
  return redirect('home')
