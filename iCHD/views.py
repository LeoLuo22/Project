from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.db.utils import IntegrityError
from django.utils import timezone
#from .models import User
from django.contrib.auth.models import User
from .models import Blog
# Create your views here.
def index(request):
    return render(request, 'iCHD/index.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        return HttpResponse('Success')
    else:
        return render(request, 'iCHD/regist.html')

def regist(request):
    return render(request, 'iCHD/regist.html')

def main(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        u = User.objects.create_user(username, password)
    except IntegrityError as err:
        return render(request, 'iCHD/regist.html', {'error_message': '该用户名已被注册'})
    u.save
    return HttpResponse("Ok")

def user(request):
    title = request.POST['title']
    body = request.POST['body']
    time = timezone.now()
    b = Blog(title=title, body=body, time=time)
    b.save()
    return HttpResponse("<h1>" + title + "</h1>" + "<h2>" + body + "</h2>")

def wel(request):
    return render(request, 'iCHD/wel.html')
