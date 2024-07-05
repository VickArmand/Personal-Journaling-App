from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
from .models import Journal

def index(request):
    """"""
    categories = Journal.objects.all()
    return HttpResponse(categories)

def create(request):
    """"""
    jid = request.POST['category_id']
    uid = request.POST['user_id']
    title = request.POST['title']
    content = request.POST['content']
    if not (jid and uid and title and content):
        return HttpResponseBadRequest('Please fill in all fields')
    journal = Journal(title=title, user_id=uid, category_id=jid, content=content)
    journal.save()
    return HttpResponse('Journal Created')

def edit(request, id):
    """"""
    jid = id
    if not id:
        return HttpResponseBadRequest("Invalid Journal ID")
    jcontent = request.PUT['content']
    journal = Journal.objects.get(id=jid)
    if not journal:
        return HttpResponseBadRequest("Journal not found")
    journal.content = jcontent
    journal.save()
    return HttpResponse('Journal edited')

def find(request, id):
    """"""
    jid = id
    journal = Journal.objects.get(id=jid)
    return HttpResponse(journal)

def delete(request, id):
    """"""
    jid = id
    if not id:
        return HttpResponseBadRequest("Invalid Journal ID")
    journal = Journal.objects.get(id=jid)
    if not journal:
        return HttpResponseBadRequest("Journal not found")
    journal.delete()
    return HttpResponse('Journal Deleted')
