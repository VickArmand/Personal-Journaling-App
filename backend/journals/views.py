from django.shortcuts import render
from django.http import HttpResponse
from models import Journal

def index(request):
    """"""
    categories = Journal.objects.all()
    return HttpResponse(categories)

def create(request):
    """"""
    cname = request.POST['name']
    journal = Journal(name=cname)
    journal.save()
    return HttpResponse('Journal Created')

def edit(request, id):
    """"""
    cid = id
    jcontent = request.PUT['content']
    journal = Journal.objects.get(id=cid)
    journal.content = jcontent
    journal.save()
    return HttpResponse('Journal edited')

def find(request, id):
    """"""
    cid = id
    journal = Journal.objects.get(id=cid)
    return HttpResponse(Journal)

def delete(request, id):
    """"""
    cid = id
    journal = Journal.objects.get(id=cid)
    journal.delete()
    return HttpResponse('Journal Deleted')
