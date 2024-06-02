from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
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
        username=request.data['username']
    )
    user.set_password(request.data['password'])
    user.save()
    profile = Profile.objects.create(
        user=user,
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )
    profile.save()
    bookshelf = Bookshelf.objects.create(
        profile=profile
    )
    profile.bookshelf = bookshelf
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_bookshelf(request):
    try:
        if 'id' in request.data:
            book_id = request.data['id']
            book = Books.objects.get(id=book_id)
            bookshelf = request.user.profile.bookshelf
            bookshelf.books.add(book)
            return Response({"message": "Book added to bookshelf successfully"}, status=200)
        else:
            return Response({"error": "Book ID not provided in request"}, status=400)
    except Books.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)
    except Bookshelf.DoesNotExist:
        return Response({"error": "Bookshelf not found for user"}, status=404)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def get_books(request):
    if request.method == 'POST':
        if 'id' in request.data:
            book = Books.objects.filter(id=request.data['id']).first()
            serialize_books = BookSerializer(book)
            return Response(serialize_books.data)
        else:
            book = Books.objects.create(
                title=request.data['title'],
                author=request.data['author'],
                genre=request.data['genre']
            )
            serialize_books = BookSerializer(book)
            return Response(serialize_books.data)
    elif request.method == 'GET':
        books = Books.objects.all()
        serialize_books = BookSerializer(books, many=True)
        return Response(serialize_books.data)
    elif request.method == 'PUT':
        book = Books.objects.filter(id=request.data['id']).first()
        if book:
            book.title = request.data.get('title', book.title)
            book.author = request.data.get('author', book.author)
            book.genre = request.data.get('genre', book.genre)
            book.save()
            serialize_books = BookSerializer(book)
            return Response(serialize_books.data)
        else:
            return Response({"error": "Book not found"}, status=404)
    elif request.method == 'DELETE':
        book = Books.objects.filter(id=request.data['id']).first()
        if book:
            book.delete()
            return Response(status=204)
        else:
            return Response({"error": "Book not found"}, status=404)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def add_book(request):
    try:
        user = request.user
        profile = user.profile
        bookshelf = profile.bookshelf
        book = Books.objects.get(author=request.data['author'], title=request.data['title'])
        bookshelf.books.add(book)
        return Response(status=204)
    except Books.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)
    except Bookshelf.DoesNotExist:
        return Response({"error": "Bookshelf not found for user"}, status=404)


@api_view(['POST'])
@permission_classes([])
def create_book(request):
    book = Books.objects.create(
        title=request.data['title'],
        author=request.data['author'],
        genre=request.data['genre']
    )
    book.save()
    book_serializer = BookSerializer(book)
    return Response(book_serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_book(request):
    try:
        book = Books.objects.get(id=request.data['id'])
        book.title = request.data['title']
        book.author = request.data['author']
        book.genre = request.data['genre']
        book.save()
        book_update_serializer = BookSerializer(book)
        return Response(book_update_serializer.data)
    except Books.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    review = BookReview.objects.create(
        user=request.user,
        book_id=request.data['book'],
        review=request.data['review'],
        rating=request.data['rating']
    )
    review.save()
    review_serializer = BookReviewSerializer(review)
    return Response(review_serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_book_reviews(request, book_id):
    try:
        book = Books.objects.get(id=book_id)
        reviews = BookReview.objects.filter(book=book)
        serialized_reviews = BookReviewSerializer(reviews, many=True)
        return Response(serialized_reviews.data)
    except Books.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)