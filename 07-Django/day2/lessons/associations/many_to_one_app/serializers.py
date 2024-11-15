from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    # author = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id','name','author']

    # def get_author(self,instance):
    #     author_name = instance.author
    #     return author_name

class AuthorSerializer(serializers.ModelSerializer):
    # novels = BookSerializer()
    novels = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ['id','name','novels']
        
    class get_novels(self,instance):
        books = instance.novels.all()
        ser_books = [{'id':books.id, 'title':books.titel} for book in books]
        return ser_books