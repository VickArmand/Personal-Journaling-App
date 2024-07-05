from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Category

def index(request):
    """"""
    categories = Category.objects.all()
    return HttpResponse(categories)

def create(request):
    """"""
    cname = request.POST['name']
    if not cname:
        return HttpResponseBadRequest('Category Name Required')
    category = Category(name=cname)
    category.save()
    return HttpResponse('Category Created'), 201

def edit(request, id):
    """"""
    cid = id
    if not id:
        return HttpResponseBadRequest("Invalid Category ID")
    category = Category.objects.get(id=cid)
    if not category:
        return HttpResponseBadRequest("Category not found")
    cname = request.PUT['name']
    if cname:
        category.name = cname
        category.save()
    return HttpResponse('Category edited')

def find(request, id):
    """"""
    cid = id
    category = Category.objects.get(id=cid)
    return HttpResponse(category)

def delete(request, id):
    """"""
    cid = id
    if not id:
        return HttpResponseBadRequest("Invalid Category ID")
    category = Category.objects.get(id=cid)
    if not category:
        return HttpResponseBadRequest("Category not found")
    category.delete()
    return HttpResponse('Category Deleted')
