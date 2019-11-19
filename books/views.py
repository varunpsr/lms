from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import Book, Author, Publication, Language
from .serializers import BookSerializer, AuthorSerializer, PublicationSerializer, LanguageSerializer


@api_view(['GET', 'POST', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def book_list(request):
    """
    List all books or create a new book
    """
    try:
        books = Book.objects.all()
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def api_update_book_view(request, id):
    """
    Update a book object.
    """
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update Successful."
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
def api_view_delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        operation = book.delete()
        data = {}
        if operation:
            data["success"] = "Delete Successful"
        else:
            data["failure"] = "Delete Failed"
        return Response(data, status=status.HTTP_200_OK)

# @api_view(['POST', ])
# def api_create_book_view(request):
#     """
#     Create a book object.
#     """
#     data = {}
#     if request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data["success"] = "Creation Successful."
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
