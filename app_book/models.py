from django.db import models
from django.contrib.auth.models import User

class Books (models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField()
    last_name = models.TextField()
    favorite_books = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username