from django.urls import path
from . import views

urlpatterns = [
    path('api/books/', views.BookListCreate.as_view()),
]
