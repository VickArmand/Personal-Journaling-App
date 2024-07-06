from django.shortcuts import render
from django.http import JsonResponse
from .models import Category
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CategorySerializer

@api_view(['GET'])
def index(request):
    """"""
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST'])
def create(request):
    """"""
    serializer = CategorySerializer(data=request.data)
    if not serializer.is_valid():
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
    serializer.save()
    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def edit(request, id):
    """"""
    cid = id
    try:
        category = Category.objects.get(id=cid)
    except Category.DoesNotExist:
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category, data=request.data)
    if not serializer.is_valid():
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def find(request, id):
    """"""
    cid = id
    try:
        category = Category.objects.get(id=cid)
    except Category.DoesNotExist:
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete(request, id):
    """"""
    cid = id
    try:
        category = Category.objects.get(id=cid)
    except Category.DoesNotExist:
        return JsonResponse({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    category.delete()
    return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
