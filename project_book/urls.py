"""
URL configuration for project_book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app_book.views import *

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', get_profile),
    path('update-book', update_book),
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('create-user/', create_user),
    path('get-books/', get_books),
    path('create-book', create_book),
    path('', include(router.urls)),
    path('create-review/', create_review, name='create-review'),
    path('book/<int:book_id>/reviews/', get_book_reviews, name='get-book-reviews'),
    path('add-to-bookshelf/', add_to_bookshelf, name='add-to-bookshelf')
]
