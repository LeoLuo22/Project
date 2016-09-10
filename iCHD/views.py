from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.db.utils import IntegrityError
from django.utils import timezone
#from .models import User
from django.contrib.auth.models import User
from .models import Blog, Comment
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

def add(request):
    title = request.POST.get('title')
    body = request.POST.get('content')
    time = timezone.now()
    b = Blog(id=1, title=title, body=body, time=time)
    b.save()
    return HttpResponse("<h1>" + title + "</h1>" + "<h2>" + body + "</h2>")

def wel(request):
    return render(request, 'iCHD/wel.html')

def post(request):
    return render(request, 'iCHD/post.html')

def detail(request):
    b = Blog.objects.get(id=1)
    return render(request, 'iCHD/blog/detail.html', {'blog':b})

def delete(request):
    b = Blog.objects.get(id=1)
    b.delete()
    return HttpResponse("删除成功")

def all(request):
    blogs = Blog.objects.all()
    return render(request, 'iCHD/all.html', {'blogs':blogs})

def detail(request, title):
    blog = Blog.objects.get(title=title)
    return HttpResponse( "<h1>" + blog.title+ "</h1>" + "</br>" + blog.body + "<a href='/iCHD/blog/" + blog.title  + "/comment" + "'"">" + "评论" + "</a>")

def comment(request, title):
    return render(request, 'iCHD/comment.html', {'title': title})

def comment_add(request, title):
    b = Blog.objects.get(title=title)
    comment = request.POST['content']
    b.comment_set.create(comment=comment)
    return HttpResponse(comment)

