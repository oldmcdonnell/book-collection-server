from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import viewsets

from .models import *
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serialized_profile = ProfileSerializer(profile)
    return Response(serialized_profile.data)

@api_view(['POST'])
@permission_classes([])
def create_user(request):
    user = User.objects.create(
        username = request.data['username']
    )
    user.set_password(request.data['password'])
    user.save()
    profile = Profile.objects.create(
        user = user,
        first_name = request.data['first_name'],
        last_name = request.data['last_name']
    )
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def get_books(request):
    if request.method == 'POST' and request.data['id']:
        book = Books.objects.filter(id = request.data['id']).first()
        serialize_books = BookSerializer(book)
        print('hit ID 2 ', serialize_books.data)
        return Response(serialize_books.data)
    elif request.method == 'POST':
        book = Books.objects.create(
            title = request.data['title'],
            author = request.data['author'],
            genre= request.data['genre']
        )
        serialize_books = BookSerializer(book)
        print('hit ID 2 ', serialize_books.data)
        return Response(serialize_books.data)
    elif request.method == 'GET':
        print('Request all book data', request)
        book = Books.objects.all()
        serialize_books = BookSerializer(book, many=True)
        return Response(serialize_books.data)
    elif request.method == 'PUT':
        book = Books.objects.filter(id = request.data['id']).first()
        if (request.data['title'].exists()):
            book.title = request.data['title']
        if (request.data['author'].exists()):
            book.author = request.data['author']
        if (request.data['genre'].exists):
            book.genre = request.data['genre']
        book.save()
        serialize_books = BookSerializer(book)
        return Response(serialize_books.data)
    elif request.method == 'DELETE':
        book = Books.objects.filter(id = request.data['id']).first()
        serialize_books = BookSerializer(book)
        return Response(serialize_books.data)
    # print('REQUEST: ', request.data)
    # books = Books.objects.all()
    # serialize_books = BookSerializer(books, many = True)
    # return Response(serialize_books.data)


@api_view(['PUT'])
@permission_classes([])
def add_book(request):
    print('Add book', request)
    user = request.user
    profile = user.profile
    bookshelf = profile.bookshelf
    books = bookshelf.books
    book = Books.objects.get(author= request.data['author'], title = request.data['title'])
    books.add(book)


@api_view(['POST'])
@permission_classes([])
def create_book(request):
    book = Books.objects.create(
        title = request.data['title'],
        author = request.data['author'],
        genre = request.data['genre'],
    )
    book.save()
    book_serializer = BookSerializer(book)
    return Response(book_serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

@api_view(['PUT'])
@permission_classes([])
def update_book(request):
    book = Books.objects.filter(id)
    book.title = request.data['title'],
    book.author = request.data['author'],
    book.genre = request.data['genre']
    book.save()
    book_update_serializer = BookSerializer(book)
    return Response(book_update_serializer.data)

