from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Change 1 to the id of a real user in your database
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default="")

    def __str__(self):
        return f'{self.title} by {self.author}'
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField()
    last_name = models.TextField()
    favorite_books = models.ManyToManyField(Books, null=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Bookshelf(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='bookshelf')
    books = models.ManyToManyField(Books)

    def __str__(self):
        return f"Bookshelf of {self.profile.user.username}"