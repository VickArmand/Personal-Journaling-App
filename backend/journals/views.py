from django.shortcuts import render
from django.http import JsonResponse
from .models import Journal
from .serializers import JournalSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    """"""
    journals = Journal.objects.all()
    serializer = JournalSerializer(journals, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    """"""
    serializer = JournalSerializer(data=request.data)
    if not serializer.is_valid():
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
    serializer.save()
    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def find(request, id):
    """"""
    cid = id
    try:
        journal = Journal.objects.get(id=cid)
    except Journal.DoesNotExist:
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
    serializer = JournalSerializer(journal)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def summary(request):
    """"""
    from datetime import datetime
    current_time = datetime.now()
    journals_year = Journal.objects.filter(created_at__year = current_time.year)
    journals_month = journals_year.filter(created_at__month=current_time.month)
    journals_day = journals_year.filter(created_at__day=current_time.day)
    week_start = current_time.day - current_time.weekday()
    week_end = week_start + 6
    journals_week = journals_year.filter(created_at__day__gt=week_start).filter(created_at__day__lt=week_end)

    summary = {
        "year": journals_year.count(),
        "month": journals_month.count(),
        "week": journals_week.count(),
        "day": journals_day.count(),
    }
    return JsonResponse(summary, status=status.HTTP_200_OK, safe=False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    """"""
    cid = id
    try:
        journal = Journal.objects.get(id=cid)
    except Journal.DoesNotExist:
        return JsonResponse({"error": "Journal not found"}, status=status.HTTP_404_NOT_FOUND)
    journal.delete()
    return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
