from django.shortcuts import render
from django.http import JsonResponse
from .models import Journal
from .serializers import JournalSerializer
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    """"""
    journals = Journal.objects.all()
    serializer = JournalSerializer(journals, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST'])
def create(request):
    """"""
    serializer = JournalSerializer(data=request.data)
    if not serializer.is_valid():
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
    serializer.save()
    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def edit(request, id):
    """"""
    cid = id
    try:
        journal = Journal.objects.get(id=cid)
    except Journal.DoesNotExist:
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
    serializer = JournalSerializer(journal, data=request.data)
    if not serializer.is_valid():
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def find(request, id):
    """"""
    cid = id
    try:
        journal = Journal.objects.get(id=cid)
    except Journal.DoesNotExist:
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
    serializer = JournalSerializer(journal)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete(request, id):
    """"""
    cid = id
    try:
        journal = Journal.objects.get(id=cid)
    except Journal.DoesNotExist:
        return JsonResponse({"error": "Journal not found"}, status=status.HTTP_404_NOT_FOUND)
    journal.delete()
    return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
