from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='novels')

"""    
from one_to_one_app.serializers import AuthorSerializer, BookSerializer

stephen = Author(name='stephen King')
stephen.fullclean()
stephen.save()
stephen

it = Book(title='It', author=stephen)
it.fullclean()
it.save()
it

ser_stephen = AuthorSerializer(stephen)
ser_stephen.data

ser_book = BookSerializizer(it)
ser_book.data

it.title
it.author
it.author.name
stephen.name
stephen.author
stephen.novels

holly = Book(name="Holly", author=stephen)
holly.full_clean()
holly.save()
stephen.novels

stephen.novels.all()
"""


"""
from one_to_one_app.serializers import AuthorSerializer, BookSerializer
ser_s = AuthorSerializer(Author.objects.get(id=1))
ser_s.data

ser_book = BookSerializer(Book.objects.get(id=1))
ser_book.data
"""


"""
from one_to_one_app.serializers import AuthorSerializer, BookSerializer
ser_book = BookSerializer(Book.objects.get(id=1))
ser_book

"""
