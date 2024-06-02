from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = '__all__'

class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = '__all__'