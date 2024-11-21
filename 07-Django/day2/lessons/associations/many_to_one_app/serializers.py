from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']

    def get_author(self, instance):
        author_name = instance.author.name
        return author_name

class AuthorSerializer(serializers.ModelSerializer):
    novels = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ['id', 'name', 'novels']

    def get_novels(self, instance):
        books = instance.novels.all()
        ser_books = [{'id':book.id, 'title':book.title} for book in books]
        return ser_books