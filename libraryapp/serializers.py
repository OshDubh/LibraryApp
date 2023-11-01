# serializers.py created inside your app folder
from rest_framework import serializers
from .models import *

class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ['id', 'year', 'author', 'price', 'title', 'synopsis', 'category', 'copies']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = ['id', 'name']

class BorrowSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Borrow
		fields = ['id', 'book_id', 'customer_id', 'due_date']