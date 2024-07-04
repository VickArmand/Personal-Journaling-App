from django.shortcuts import render
from django.http import HttpResponse
from models import Category

def index(request):
    """"""
    categories = Category.objects.all()
    return HttpResponse(categories)

def create(request):
    """"""
    cname = request.POST['name']
    category = Category(name=cname)
    category.save()
    return HttpResponse('Category Created')

def edit(request, id):
    """"""
    cid = id
    category = Category.objects.get(id=cid)
    category.delete()
    return HttpResponse('Category edited')

def find(request, id):
    """"""
    cid = id
    category = Category.objects.get(id=cid)
    return HttpResponse(category)

def delete(request, id):
    """"""
    cid = id
    category = Category.objects.get(id=cid)
    category.delete()
    return HttpResponse('Category Deleted')
