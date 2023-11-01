#	imports for forms.py 
from django import forms
from .models import * # import all of your models
import datetime

# the form for submitting a book
class BookForm(forms.ModelForm):
	class Meta:
			model = Book
			fields = ["year", "author", "price", "title", "synopsis", "category", "copies"]
	

	# sanitise the input
	def clean(self):
		data = self.cleaned_data
		model = Book

		# extract the info from the form
		year = data["year"]
		author = data["author"]
		price = data["price"]
		title = data["title"]
		synopsis = data["synopsis"]
		category = data["category"]
		copies = data["copies"]

		book_exists = Book.objects.filter(title = title).exists() # check if we have the book in our library already
		valid_year = year <= datetime.datetime.today().year # check if the date we have entered is in the future (not allowed)
		
		model_price = (model._meta.get_fields())
		valid_price = price < 1000 # checking that the price is less than the max length in the model
		editing = self.instance.id is not None # id exists if we are editing

		if not valid_year:
			raise forms.ValidationError("Please enter a publishing year in the past")

		elif not valid_price:
			raise forms.ValidationError("Please add a price in the range €1-999")

		elif book_exists and not editing:
			raise forms.ValidationError("We already have that book in our library!")

		return data # return the sanitised input
