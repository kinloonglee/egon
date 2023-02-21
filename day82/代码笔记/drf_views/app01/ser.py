

from rest_framework import serializers
from app01.models import Book,Publish
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publish
        fields='__all__'
