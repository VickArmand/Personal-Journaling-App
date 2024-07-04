from django.shortcuts import render
from django.http import HttpResponse
from models import User

def index(request):
    """"""
    categories = User.objects.all()
    return HttpResponse(categories)

def create(request):
    """"""
    cname = request.POST['name']
    User = User(name=cname)
    User.save()
    return HttpResponse('User Created')

def edit(request, id):
    """"""
    cid = id
    User = User.objects.get(id=cid)
    User.delete()
    return HttpResponse('User edited')

def find(request, id):
    """"""
    cid = id
    User = User.objects.get(id=cid)
    return HttpResponse(User)

def delete(request, id):
    """"""
    cid = id
    User = User.objects.get(id=cid)
    User.delete()
    return HttpResponse('User Deleted')
