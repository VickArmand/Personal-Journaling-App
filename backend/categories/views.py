from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Category
from rest_framework.decorators import api_view
from .serializers import CategorySerializer
from uuid import uuid4

def index(request):
    """"""
    categories = Category.objects.all()
    return HttpResponse(categories)

@api_view(['POST'])
def create(request):
    """"""
    request.data.id = str(uuid4())
    serializer = CategorySerializer(data=request.data)
    if not serializer.is_valid():
        return HttpResponseBadRequest('Category Name Required')
    serializer.save()
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
