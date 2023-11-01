from django.db import models

# A template for every book we have in our library
class Book(models.Model):
	id = models.AutoField(primary_key=True)

	year = models.IntegerField()
	author = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=50, decimal_places=2)
	title = models.CharField(max_length=64)
	synopsis = models.CharField(max_length=512)
	category = models.CharField(max_length=64, default="Comedy")
	copies = models.IntegerField(default = 1) # how many copies of the book we have

	# name it on the page
	def __str__(self):
		return self.title

# A template for all the customers our library currently serves
class Customer(models.Model):
	id = models.AutoField(primary_key = True)
	name =  models.CharField(max_length = 64)

	#name it on the page
	def __str__(self):
		return self.name

# Keeping track of all the books that are being and have been borrowed, each instance is a book that has been or can be borrowed
class Borrow(models.Model):
	id = models.AutoField(primary_key = True)
	
	book_id = models.ForeignKey('Book', on_delete=models.CASCADE) # the id of the book that this instance of a borrowed book is referencing 
	customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE) # cascade means if the reference gets deleted, our instance does too
	due_date = models.DateField(editable = True)

	# name it on the page
	def __str__(self):
		return str(self.book_id) + " borrowed by " + str(self.customer_id) + ", due " + str(self.due_date) + "."