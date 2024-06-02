from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default="")

    def __str__(self):
        return f'{self.title} by {self.author}'

class Bookshelf(models.Model):
    profile = models.OneToOneField('Profile', on_delete=models.CASCADE, related_name='bookshelf_profile')
    books = models.ManyToManyField(Books)

    def __str__(self):
        return f"Bookshelf of {self.profile.user.username}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField()
    last_name = models.TextField()
    favorite_books = models.ManyToManyField(Books, blank=True)
    bookshelf = models.OneToOneField(Bookshelf)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'Review by {self.user.username} for {self.book.title}'